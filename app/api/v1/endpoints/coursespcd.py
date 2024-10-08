from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/coursespcd", tags=["CoursesPCD"])
"""Lista de PCD em que a faculdade tem disponibilidade"""


@router.get("/all/", response_model=List[schema.GetCoursesPCD], status_code=200)
def get_all_coursespcd():
    return models.CoursesPCD.get_all()


@router.get("/paginate/", response_model=List[schema.GetCoursesPCD], status_code=200)
def get_paginate_coursespcd_by_page_per_page(page: int, per_page: int):
    return models.CoursesPCD.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowCouresesPCD, status_code=200)
def get_coursespcd_by_uuid(uuid: UUID4):
    return models.CoursesPCD.get(uuid)


@router.post("/", response_model=schema.GetCoursesPCD, status_code=201)
def create_new_coursespcd(
    json_data: List[schema.PostCoursesPCD],
):
    try:
        _db = db.Session()
        for data_list in json_data:
            data = models.CoursesPCD(**data_list.dict())
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "dado não encontrado"}]
                )
            _db.add(data)
        _db.commit()
        _db.refresh(data)
    finally:
        _db.close()
    return "Ok"


@router.put("/uuid", response_model=schema.GetCoursesPCD, status_code=200)
def update_coursespcd_by_uuid(uuid: UUID4, json_data: schema.PutCoursesPCD):
    return models.CoursesPCD.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_coursespcd_by_uuid(uuid: UUID4):
    return models.CoursesPCD.remove(uuid)
