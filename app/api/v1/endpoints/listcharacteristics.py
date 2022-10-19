from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/listcharacteristics", tags=["ListCharacteristics"])


@router.get(
    "/all/", response_model=List[schema.GetListCharacteristics], status_code=200
)
def get_all_listcharacteristics():
    return models.ListCharacteristics.get_all()


@router.get(
    "/paginate/", response_model=List[schema.GetListCharacteristics], status_code=200
)
def get_paginate_listcharacteristics_by_page_per_page(page: int, per_page: int):
    return models.ListCharacteristics.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowList, status_code=200)
def get_listcharacteristics_by_uuid(uuid: UUID4):
    return models.ListCharacteristics.get(uuid)


@router.post("/", response_model=schema.GetListCharacteristics, status_code=201)
def create_new_listcharacteristics(
    json_data: List[schema.PostListCharacteristics],
):
    try:
        _db = db.Session()
        for data_list in json_data:
            data = models.ListCharacteristics(**data_list.dict())
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


@router.put("/uuid", response_model=schema.GetListCharacteristics, status_code=200)
def update_listcharacteristics_by_uuid(
    uuid: UUID4, json_data: schema.PutListCharacteristics
):
    return models.ListCharacteristics.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_listcharacteristics_by_uuid(uuid: UUID4):
    return models.ListCharacteristics.remove(uuid)
