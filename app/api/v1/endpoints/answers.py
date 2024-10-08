from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/answers", tags=["Answers"])


@router.get("/all/", response_model=List[schema.GetAnswers], status_code=200)
def get_all_answers():
    return models.Answers.get_all()

@router.get("/paginate/", response_model=List[schema.GetAnswers], status_code=200)
def get_paginate_answers_by_page_per_page(page:int, per_page: int):
    return models.Answers.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetAnswers, status_code=200)
def get_answers_by_uuid(uuid: UUID4):
    return models.Answers.get(uuid)

@router.post("/", response_model=schema.GetAnswers, status_code=201)
def create_new_answers(
    json_data: schema.PostAnswers,
):
    data = models.Answers(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetAnswers, status_code=200)
def update_answers_by_uuid(uuid: UUID4, json_data: schema.PutAnswers):
    return models.Answers.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_answers_by_uuid(uuid: UUID4):
    return models.Answers.remove(uuid)

    