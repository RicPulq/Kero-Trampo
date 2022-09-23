from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/employercharacteristics", tags=["EmployerCharacteristics"])


@router.get("/all/", response_model=List[schema.GetEmployerCharacteristics], status_code=200)
def get_all_employercharacteristics():
    return models.EmployerCharacteristics.get_all()

@router.get("/paginate/", response_model=List[schema.GetEmployerCharacteristics], status_code=200)
def get_paginate_employercharacteristics_by_page_per_page(page:int, per_page: int):
    return models.EmployerCharacteristics.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetEmployerCharacteristics, status_code=200)
def get_employercharacteristics_by_uuid(uuid: UUID4):
    return models.EmployerCharacteristics.get(uuid)

@router.post("/", response_model=schema.GetEmployerCharacteristics, status_code=201)
def create_new_employercharacteristics(
    json_data: schema.PostEmployerCharacteristics,
):
    data = models.EmployerCharacteristics(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetEmployerCharacteristics, status_code=200)
def update_employercharacteristics_by_uuid(uuid: UUID4, json_data: schema.PutEmployerCharacteristics):
    return models.EmployerCharacteristics.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_employercharacteristics_by_uuid(uuid: UUID4):
    return models.EmployerCharacteristics.remove(uuid)

    