from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/listjobprofile", tags=["ListJobProfile"])


@router.get("/all/", response_model=List[schema.GetListJobProfile], status_code=200)
def get_all_listjobprofile():
    return models.ListJobProfile.get_all()

@router.get("/paginate/", response_model=List[schema.GetListJobProfile], status_code=200)
def get_paginate_listjobprofile_by_page_per_page(page:int, per_page: int):
    return models.ListJobProfile.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.ShowJobs, status_code=200)
def get_listjobprofile_by_uuid(uuid: UUID4):
    return models.ListJobProfile.get(uuid)

@router.post("/", response_model=schema.GetListJobProfile, status_code=201)
def create_new_listjobprofile(
    json_data: List[schema.PostListJobProfile],
):
    try:
        _db = db.Session()
        for data_list in json_data:
            data = models.ListJobProfile(**data_list.dict())
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


@router.put("/uuid", response_model=schema.GetListJobProfile, status_code=200)
def update_listjobprofile_by_uuid(uuid: UUID4, json_data: schema.PutListJobProfile):
    return models.ListJobProfile.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_listjobprofile_by_uuid(uuid: UUID4):
    return models.ListJobProfile.remove(uuid)

    