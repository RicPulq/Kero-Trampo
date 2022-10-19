from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/companypcd", tags=["CompanyPcd"])


@router.get("/all/", response_model=List[schema.GetCompanyPcd], status_code=200)
def get_all_companypcd():
    return models.CompanyPcd.get_all()

@router.get("/paginate/", response_model=List[schema.GetCompanyPcd], status_code=200)
def get_paginate_companypcd_by_page_per_page(page:int, per_page: int):
    return models.CompanyPcd.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.ShowPCDs, status_code=200)
def get_companypcd_by_uuid(uuid: UUID4):
    return models.CompanyPcd.get(uuid)

@router.post("/", response_model=schema.GetCompanyPcd, status_code=201)
def create_new_companypcd(
    json_data: List[schema.PostCompanyPcd],
):
    try:
        _db = db.Session()
        for data_list in json_data:
            data = models.CompanyPcd(**data_list.dict())
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



@router.put("/uuid", response_model=schema.GetCompanyPcd, status_code=200)
def update_companypcd_by_uuid(uuid: UUID4, json_data: schema.PutCompanyPcd):
    return models.CompanyPcd.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_companypcd_by_uuid(uuid: UUID4):
    return models.CompanyPcd.remove(uuid)

    