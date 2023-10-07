from fastapi import FastAPI

from models.dtos import SearchQueryRequest, SearchByIndexRange, SearchBySinglePage, SearchByMultiplePages
from services.QdrantService import QdrantService

app = FastAPI()

service = QdrantService()


@app.post("/api/search-pdf-document")
async def search_pdf_document(request: SearchQueryRequest):
    return service.query_data(request.query, request.fetch_num, request.offset)


@app.post("/api/fetch-chunks-range")
async def fetch_chunks_range(request: SearchByIndexRange):
    return service.fetch_chunks_by_range(request.bottom_index, request.top_index)


@app.post("/api/fetch-chunks-on-page")
async def fetch_chunks_on_page(request: SearchBySinglePage):
    return service.fetch_chunks_on_specific_page(request.page)


@app.post("/api/fetch-chunks-on-multiple-pages")
async def fetch_chunks_on_multiple_pages(request: SearchByMultiplePages):
    return service.fetch_chunks_on_specific_pages(request.page)
