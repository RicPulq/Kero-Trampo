from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("/all/", response_model=List[schema.GetCompany], status_code=200)
def get_all_company():
    return models.Company.get_all()


@router.get("/paginate/", response_model=List[schema.GetCompany], status_code=200)
def get_paginate_company_by_page_per_page(page: int, per_page: int):
    return models.Company.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.GetCompany, status_code=200)
def get_company_by_uuid(uuid: UUID4):
    return models.Company.get(uuid)


@router.post("/", response_model=schema.GetCompany, status_code=201)
def create_new_company(
    json_data: schema.PostCompany,
):
    data = models.Company(**json_data.dict())
    return data.create()


@router.post("/v2", response_model=schema.GetCompany, status_code=201)
def create_company_with_all(
    user: schema.PostUser,
    address: schema.PostAddress,
    company: schema.PostCompany,
):
    """Para criar uma filial, usar rota BranchOffice"""
    data_user = models.User(**user.dict())
    data_company = models.Company(**company.dict())
    data_address = models.Address(**address.dict())

    data_user.company_relation.append(data_company)
    data_address.company.append(data_company)

    return data_user.create(), data_address.create()


@router.put("/uuid", response_model=schema.GetCompany, status_code=200)
def update_company_by_uuid(uuid: UUID4, json_data: schema.PutCompany):
    return models.Company.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_company_by_uuid(uuid: UUID4):
    return models.Company.remove(uuid)
