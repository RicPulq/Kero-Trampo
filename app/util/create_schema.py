from typing import Container, Optional, Type

from pydantic import BaseConfig, BaseModel
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import ColumnProperty
from app import models, schema
from .util import list_files

__all__ = ['create_schema']


class OrmConfig(BaseConfig):
    orm_mode = True

def sqlalchemy_to_pydantic(
    db_model: Type, *, config: Type = OrmConfig, exclude: Container[str] = []
) -> Type[BaseModel]:
    mapper = inspect(db_model)
    fields = {}
    for attr in mapper.attrs:
        max_length = None
        if isinstance(attr, ColumnProperty):
            if attr.columns:
                name = attr.key
                if name in exclude:
                    continue
                column = attr.columns[0]
                python_type: Optional[type] = None
                if hasattr(column.type, "impl"):
                    if hasattr(column.type.impl, "python_type"):
                        python_type = column.type.impl.python_type
                elif hasattr(column.type, "python_type"):
                    python_type = column.type.python_type
                    if hasattr(column.type, "length"):
                        max_length = f", max_length={column.type.length}"
                assert python_type, f"Could not infer python_type for {column}"
                fields[name] = f"{python_type.__name__} | {None} = Field(description='{name.capitalize()} Documentar'{max_length if max_length else ''})"
    write_schema(db_model.__name__, fields)



def write_attribute(fields, exclude: list | None = None):
    string = ""
    print(type(exclude))
    for key, value in fields.items():
        if key not in exclude:
            string += f'    {key}: {value}\n'
    return string


def write_schema(schema_name, fields):
    with open(f'app/schema/{schema_name.lower()}_schema.py', 'w') as f:
        f.write(
            f"""from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['Post{schema_name}', 'Get{schema_name}', 'Put{schema_name}',]



class Post{schema_name}(BaseModel):
{write_attribute(fields, ["uuid", "creat_at", "updat_at"])}
    

class Get{schema_name}(BaseModel):
{write_attribute(fields, [""])}

    class Config:
        orm_mode = True



class Put{schema_name}(BaseModel):
{write_attribute(fields, [""])}"""
            )

def list_imports_from_packge(package)-> list:
    list_response = []
    for key, value in package.__dict__.items():
        if str(type(value)) == "<class 'sqlalchemy.orm.decl_api.DeclarativeMeta'>":
            list_response.append(key)
        print(key)
        print(value)
        if str(type(value)) == "<class '--'>":
            list_response.append(key)
    return list_response

def write__init__(path):
    all_files = list_files(path)
    string = ""

    for file in all_files:
        if file != "__init__.py":
            string += f'from .{file.split(".")[0]} import *\n'
    with open(f'{path}/__init__.py', 'w') as f:
        f.write(
            f"""{string}"""
            )

def create_schema():
    for key, value in models.__dict__.items():
        if str(type(value)) == "<class 'sqlalchemy.orm.decl_api.DeclarativeMeta'>":
            db_models = getattr(models, f'{key}')
            sqlalchemy_to_pydantic(db_models)
    write__init__("app/schema")


# create_schema()