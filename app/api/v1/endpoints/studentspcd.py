from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/studentspcd", tags=["StudentsPcd"])


@router.get("/all/", response_model=List[schema.GetStudentsPcd], status_code=200)
def get_all_studentspcd():
    return models.StudentsPcd.get_all()

@router.get("/paginate/", response_model=List[schema.GetStudentsPcd], status_code=200)
def get_paginate_studentspcd_by_page_per_page(page:int, per_page: int):
    return models.StudentsPcd.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetStudentsPcd, status_code=200)
def get_studentspcd_by_uuid(uuid: UUID4):
    return models.StudentsPcd.get(uuid)

@router.post("/", response_model=schema.GetStudentsPcd, status_code=201)
def create_new_studentspcd(
    json_data: schema.PostStudentsPcd,
):
    data = models.StudentsPcd(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetStudentsPcd, status_code=200)
def update_studentspcd_by_uuid(uuid: UUID4, json_data: schema.PutStudentsPcd):
    return models.StudentsPcd.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_studentspcd_by_uuid(uuid: UUID4):
    return models.StudentsPcd.remove(uuid)

    