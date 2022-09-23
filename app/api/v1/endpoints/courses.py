from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/all/", response_model=List[schema.GetCourses], status_code=200)
def get_all_courses():
    return models.Courses.get_all()

@router.get("/paginate/", response_model=List[schema.GetCourses], status_code=200)
def get_paginate_courses_by_page_per_page(page:int, per_page: int):
    return models.Courses.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetCourses, status_code=200)
def get_courses_by_uuid(uuid: UUID4):
    return models.Courses.get(uuid)

@router.post("/", response_model=schema.GetCourses, status_code=201)
def create_new_courses(
    json_data: schema.PostCourses,
):
    data = models.Courses(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetCourses, status_code=200)
def update_courses_by_uuid(uuid: UUID4, json_data: schema.PutCourses):
    return models.Courses.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_courses_by_uuid(uuid: UUID4):
    return models.Courses.remove(uuid)

    