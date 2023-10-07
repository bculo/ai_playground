from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter, TextSplitter

EMBEDDING_MODEL = SentenceTransformerEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


def get_embedding_model() -> SentenceTransformerEmbeddings:
    return EMBEDDING_MODEL


def get_document_splitter() -> TextSplitter:
    return CharacterTextSplitter(
        separator="\n",
        chunk_size=1400,
        chunk_overlap=100,
        length_function=len,
    )