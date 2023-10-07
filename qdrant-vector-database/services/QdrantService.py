from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, Filter, FieldCondition, Range, MatchValue, MatchAny

from models.dtos import IndexInfo, QueryItemResponse, QueryListResponse
from utilities import llm_utilities, string_utilities


class QdrantService:

    def __init__(self):
        self.collection_name = 'TestCollection'

    def get_client(self) -> QdrantClient:
        return QdrantClient(url='http://localhost:6333')

    def get_qdrant_wrapper(self) -> Qdrant:
        embeddings = llm_utilities.get_embedding_model()
        return Qdrant(client=self.get_client(),
                      collection_name=self.collection_name,
                      embeddings=embeddings)

    def fetch_collection_stats(self) -> IndexInfo:
        client = self.get_client()
        info = client.get_collection(self.collection_name)
        return IndexInfo(self.collection_name,
                         info.config.params.vectors.distance,
                         info.config.params.vectors.size,
                         info.points_count)

    def delete_collection(self) -> None:
        client = self.get_client()
        result = client.delete_collection(collection_name=self.collection_name)
        print(f"Collection deleted: {result}")

    def create_collection(self) -> None:
        client = self.get_client()
        vector_config = VectorParams(size=768, distance=Distance.COSINE)  # mpnet-v2 produce vectors with 768 points
        result = client.create_collection(collection_name=self.collection_name, vectors_config=vector_config)
        print(f"Collection created: {result}")

    def seed_collection(self) -> None:
        loader = PyPDFLoader('./pdfs/fritzbox7590.pdf')
        text_splitter = llm_utilities.get_document_splitter()
        document_chunks = loader.load_and_split(text_splitter)
        for index, chunk in enumerate(document_chunks):
            chunk.metadata['index'] = index
            chunk.page_content = string_utilities.clean_string(chunk.page_content)
        qdrant_wrapper = self.get_qdrant_wrapper()
        qdrant_wrapper.add_documents(document_chunks)

    def query_data(self, query: str, fetch_num: int, offset: int = 0) -> QueryListResponse:
        store = self.get_qdrant_wrapper()
        search_results = store.similarity_search_with_score(query=query,
                                                            k=fetch_num,
                                                            offset=offset,
                                                            score_threshold=.5)

        response_items = []
        for result in search_results:
            [document, similarity] = result
            response_item = QueryItemResponse(document.page_content,
                                              document.metadata,
                                              similarity)
            response_items.append(response_item)

        return QueryListResponse(query, response_items)

    def fetch_chunks_by_range(self, bottom_boundary: int, top_boundary: int) -> any:
        scroll_filter = Filter(
            must=[
                FieldCondition(
                    key='metadata.index',
                    range=Range(
                        gte=bottom_boundary,
                        lte=top_boundary,
                    )
                ),
            ])

        qdrant = self.get_client()
        result = qdrant.scroll(collection_name=self.collection_name, scroll_filter=scroll_filter)
        return result

    def fetch_chunks_on_specific_page(self, page: int) -> any:
        scroll_filter = Filter(
            must=[
                FieldCondition(
                    key='metadata.page',
                    match=MatchValue(value=page)
                )
            ])

        qdrant = self.get_client()
        result = qdrant.scroll(collection_name=self.collection_name, scroll_filter=scroll_filter)
        return result

    def fetch_chunks_on_specific_pages(self, pages: list[int]) -> any:
        scroll_filter = Filter(
            must=[
                FieldCondition(
                    key='metadata.page',
                    match=MatchAny(any=pages)
                )
            ])

        qdrant = self.get_client()
        result = qdrant.scroll(collection_name=self.collection_name, scroll_filter=scroll_filter)
        return result

