from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/campus", tags=["Campus"])


@router.get("/all/", response_model=List[schema.GetCampus], status_code=200)
def get_all_campus():
    return models.Campus.get_all()

@router.get("/paginate/", response_model=List[schema.GetCampus], status_code=200)
def get_paginate_campus_by_page_per_page(page:int, per_page: int):
    return models.Campus.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetCampus, status_code=200)
def get_campus_by_uuid(uuid: UUID4):
    return models.Campus.get(uuid)

@router.post("/", response_model=schema.GetCampus, status_code=201)
def create_new_campus(
    json_data: schema.PostCampus,
):
    data = models.Campus(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetCampus, status_code=200)
def update_campus_by_uuid(uuid: UUID4, json_data: schema.PutCampus):
    return models.Campus.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_campus_by_uuid(uuid: UUID4):
    return models.Campus.remove(uuid)

    