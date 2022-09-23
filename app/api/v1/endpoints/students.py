from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/all/", response_model=List[schema.GetStudents], status_code=200)
def get_all_students():
    return models.Students.get_all()

@router.get("/paginate/", response_model=List[schema.GetStudents], status_code=200)
def get_paginate_students_by_page_per_page(page:int, per_page: int):
    return models.Students.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetStudents, status_code=200)
def get_students_by_uuid(uuid: UUID4):
    return models.Students.get(uuid)

@router.post("/", response_model=schema.GetStudents, status_code=201)
def create_new_students(
    json_data: schema.PostStudents,
):
    data = models.Students(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetStudents, status_code=200)
def update_students_by_uuid(uuid: UUID4, json_data: schema.PutStudents):
    return models.Students.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_students_by_uuid(uuid: UUID4):
    return models.Students.remove(uuid)

    