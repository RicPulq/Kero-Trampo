from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/all/", response_model=List[schema.GetQuestions], status_code=200)
def get_all_questions():
    return models.Questions.get_all()

@router.get("/paginate/", response_model=List[schema.GetQuestions], status_code=200)
def get_paginate_questions_by_page_per_page(page:int, per_page: int):
    return models.Questions.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetQuestions, status_code=200)
def get_questions_by_uuid(uuid: UUID4):
    return models.Questions.get(uuid)

@router.post("/", response_model=schema.GetQuestions, status_code=201)
def create_new_questions(
    json_data: schema.PostQuestions,
):
    data = models.Questions(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetQuestions, status_code=200)
def update_questions_by_uuid(uuid: UUID4, json_data: schema.PutQuestions):
    return models.Questions.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_questions_by_uuid(uuid: UUID4):
    return models.Questions.remove(uuid)

    