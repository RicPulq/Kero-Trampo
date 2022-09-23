from fastapi import APIRouter, Query
from pydantic.types import UUID4
from typing import List

from app import schema, models, core, util

router = APIRouter(prefix="/developer", tags=["Dev"])

@router.get("/", status_code=200)
def list_all_database_name():
    response = []
    for key, value in models.__dict__.items():
        if str(type(value)) == "<class 'sqlalchemy.orm.decl_api.DeclarativeMeta'>":
            response.append(key)    
    return response


@router.post("/generate/", status_code=201)
def generate_schema_and_endpoints(
    generate_schema: bool, generate_endpoits: bool
):
    if generate_schema:
        util.create_schema()
    if generate_endpoits:
        util.create_endpoints()
    return " "
