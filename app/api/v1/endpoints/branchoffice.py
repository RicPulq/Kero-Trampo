from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/branchoffice", tags=["BranchOffice"])


@router.get("/all/", response_model=List[schema.GetBranchOffice], status_code=200)
def get_all_branchoffice():
    return models.BranchOffice.get_all()

@router.get("/paginate/", response_model=List[schema.GetBranchOffice], status_code=200)
def get_paginate_branchoffice_by_page_per_page(page:int, per_page: int):
    return models.BranchOffice.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetBranchOffice, status_code=200)
def get_branchoffice_by_uuid(uuid: UUID4):
    return models.BranchOffice.get(uuid)

@router.post("/", response_model=schema.GetBranchOffice, status_code=201)
def create_new_branchoffice(
    json_data: schema.PostBranchOffice,
):
    data = models.BranchOffice(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetBranchOffice, status_code=200)
def update_branchoffice_by_uuid(uuid: UUID4, json_data: schema.PutBranchOffice):
    return models.BranchOffice.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_branchoffice_by_uuid(uuid: UUID4):
    return models.BranchOffice.remove(uuid)

    