from typing import Container, Optional, Type

from pydantic import BaseConfig, BaseModel
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import ColumnProperty
from app import schema, models
from .util import list_files

__all__ = ['create_endpoints']


def write__init__endpoits(path):
    all_files = list_files(path)
    import_string = ""
    use_imports = ""
    for file in all_files:
        if file != "__init__.py":
            import_string += f'from .{file.split(".")[0]} import router as {file.split(".")[0]}_router\n'
            use_imports += f'routers.include_router({file.split(".")[0]}_router)\n'
    with open(f'{path}/__init__.py', 'w') as f:
        f.write(
            f"""from fastapi import APIRouter

{import_string}

routers = APIRouter()

{use_imports}"""
            )

def create_endpoints():
    path = "app/api/v1/endpoints/"
    for key, value in models.__dict__.items():
        if str(type(value)) == "<class 'sqlalchemy.orm.decl_api.DeclarativeMeta'>":
            with open(f'{path}{key.lower()}.py', 'w') as f:
                f.write(generate_endpoints(key))
    write__init__endpoits(path)

def generate_endpoints(name: str):
    name_l = name.lower()
    uuid = "uuid"
    string_data = f"""from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/{name_l}", tags=["{name}"])


@router.get("/all/", response_model=List[schema.Get{name}], status_code=200)
def get_all_{name_l}():
    return models.{name}.get_all()

@router.get("/paginate/", response_model=List[schema.Get{name}], status_code=200)
def get_paginate_{name_l}_by_page_per_page(page:int, per_page: int):
    return models.{name}.get_paginate(page, per_page)

@router.get("/{uuid}", response_model=schema.Get{name}, status_code=200)
def get_{name_l}_by_uuid(uuid: UUID4):
    return models.{name}.get(uuid)

@router.post("/", response_model=schema.Get{name}, status_code=201)
def create_new_{name_l}(
    json_data: schema.Post{name},
):
    data = models.{name}(**json_data.dict())
    return data.create()


@router.put("/{uuid}", response_model=schema.Get{name}, status_code=200)
def update_{name_l}_by_uuid(uuid: UUID4, json_data: schema.Put{name}):
    return models.{name}.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/{uuid}", status_code=204)
def delete_{name_l}_by_uuid(uuid: UUID4):
    return models.{name}.remove(uuid)

    """
    return string_data