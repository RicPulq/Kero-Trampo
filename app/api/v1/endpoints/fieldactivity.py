from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/fieldactivity", tags=["FieldActivity"])


@router.get("/all/", response_model=List[schema.GetFieldActivity], status_code=200)
def get_all_fieldactivity():
    return models.FieldActivity.get_all()

@router.get("/paginate/", response_model=List[schema.GetFieldActivity], status_code=200)
def get_paginate_fieldactivity_by_page_per_page(page:int, per_page: int):
    return models.FieldActivity.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetFieldActivity, status_code=200)
def get_fieldactivity_by_uuid(uuid: UUID4):
    return models.FieldActivity.get(uuid)

@router.post("/", response_model=List[schema.GetFieldActivity], status_code=201)
def create_new_fieldactivity(
    json_data: List[schema.PostFieldActivity],
):
    try:
        _db = db.Session()
        for data_json in json_data:
            data = models.FieldActivity(**data_json.dict())
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "dado não encontrado"}]
                )
            _db.add(data)
        _db.flush()
        _db.refresh(data)
    finally:
        _db.close()
    return "Ok"


@router.put("/uuid", response_model=schema.GetFieldActivity, status_code=200)
def update_fieldactivity_by_uuid(uuid: UUID4, json_data: schema.PutFieldActivity):
    return models.FieldActivity.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_fieldactivity_by_uuid(uuid: UUID4):
    return models.FieldActivity.remove(uuid)

    