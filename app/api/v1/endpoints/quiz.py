from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/quiz", tags=["Quiz"])


@router.get("/all/", response_model=List[schema.GetQuiz], status_code=200)
def get_all_quiz():
    return models.Quiz.get_all()

@router.get("/paginate/", response_model=List[schema.GetQuiz], status_code=200)
def get_paginate_quiz_by_page_per_page(page:int, per_page: int):
    return models.Quiz.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetQuiz, status_code=200)
def get_quiz_by_uuid(uuid: UUID4):
    return models.Quiz.get(uuid)

@router.post("/", response_model=schema.GetQuiz, status_code=201)
def create_new_quiz(
    json_data: schema.PostQuiz,
):
    data = models.Quiz(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetQuiz, status_code=200)
def update_quiz_by_uuid(uuid: UUID4, json_data: schema.PutQuiz):
    return models.Quiz.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_quiz_by_uuid(uuid: UUID4):
    return models.Quiz.remove(uuid)

    