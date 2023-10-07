from pydantic import BaseModel


class IndexInfo:

    def __init__(self, name, metric, dimensions, vector_count):
        self.name = name,
        self.metric = metric
        self.dimensions = dimensions
        self.vector_count = vector_count


class QueryListResponse:

    def __init__(self, input_query, response_items):
        self.embedding_query = input_query
        self.items = response_items


class QueryItemResponse:

    def __init__(self, content, metadata, similarity_percentage):
        self.doc_content = content
        self.doc_metadata = metadata
        self.similarity_perc = similarity_percentage


class SearchQueryRequest(BaseModel):
    query: str = None
    fetch_num: int = 2
    offset: int = 0


class SearchByIndexRange(BaseModel):
    bottom_index: int
    top_index: int


class SearchBySinglePage(BaseModel):
    page: int


class SearchByMultiplePages(BaseModel):
    page: list[int]

