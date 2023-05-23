from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/pcd", tags=["Pcd"])


@router.get("/all/", response_model=List[schema.GetPcd], status_code=200)
def get_all_pcd():
    return models.Pcd.get_all()

@router.get("/paginate/", response_model=List[schema.GetPcd], status_code=200)
def get_paginate_pcd_by_page_per_page(page:int, per_page: int):
    return models.Pcd.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetPcd, status_code=200)
def get_pcd_by_uuid(uuid: UUID4):
    return models.Pcd.get(uuid)

@router.post("/", response_model=schema.GetPcd, status_code=201)
def create_new_pcd(
    json_data: schema.PostPcd,
):
    data = models.Pcd(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetPcd, status_code=200)
def update_pcd_by_uuid(uuid: UUID4, json_data: schema.PutPcd):
    return models.Pcd.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_pcd_by_uuid(uuid: UUID4):
    return models.Pcd.remove(uuid)

    