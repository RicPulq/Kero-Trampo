from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/academicprofiles", tags=["AcademicProfiles"])


@router.get("/all/", response_model=List[schema.GetAcademicProfiles], status_code=200)
def get_all_academicprofiles():
    return models.AcademicProfiles.get_all()

@router.get("/paginate/", response_model=List[schema.GetAcademicProfiles], status_code=200)
def get_paginate_academicprofiles_by_page_per_page(page:int, per_page: int):
    return models.AcademicProfiles.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetAcademicProfiles, status_code=200)
def get_academicprofiles_by_uuid(uuid: UUID4):
    return models.AcademicProfiles.get(uuid)

@router.post("/", response_model=schema.GetAcademicProfiles, status_code=201)
def create_new_academicprofiles(
    json_data: schema.PostAcademicProfiles,
):
    data = models.AcademicProfiles(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetAcademicProfiles, status_code=200)
def update_academicprofiles_by_uuid(uuid: UUID4, json_data: schema.PutAcademicProfiles):
    return models.AcademicProfiles.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_academicprofiles_by_uuid(uuid: UUID4):
    return models.AcademicProfiles.remove(uuid)

    