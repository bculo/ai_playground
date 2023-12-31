from typing import Annotated
from fastapi import APIRouter, Body, Depends

from sqlalchemy.orm import Session
from common.dependencies import get_db
from routers.students_models import CreateUser

from storage import students_crud
from storage.models import Student


router = APIRouter(
    prefix="/students",
    tags=["students"]
)


@router.get("/all", description="Fetch all users")
async def all_users(db: Session = Depends(get_db)):
    return students_crud.get_all(db)


@router.post("/add", description="Create new user")
async def create_user(request: Annotated[CreateUser, Body()], db: Session = Depends(get_db)):
    entity = Student(**request.model_dump())
    return students_crud.create(db, entity)