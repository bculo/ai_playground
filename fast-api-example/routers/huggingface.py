from typing import Annotated
from fastapi import APIRouter, Body, Depends

from sqlalchemy.orm import Session
from common.dependencies import get_db
from common.hf_models import get_text_classification_model
from routers.huggingface_models import TextClassificationRequest

from storage import students_crud
from storage.models import Student


router = APIRouter(
    prefix="/huggingface",
    tags=["huggingface"]
)


@router.post("/text-classification", description="Do text classification")
async def text_classification(request: Annotated[TextClassificationRequest, Body()]):
    hf_model = get_text_classification_model()
    return hf_model(request.text)
