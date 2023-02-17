from uuid import UUID
from pydantic import BaseModel, Field, validator
from datetime import datetime
from app import util

from app.schema.address_schema import GetAddress

__all__ = ['PostCampus', 'GetCampus', 'PutCampus','ShowCampus']



class PostCampus(BaseModel):
    name: str | None = Field(description='Name Documentar', max_length=255)
    # address_uuid: UUID | None = Field(description='Address_uuid Documentar')
    name_institution: str | None = Field(description='Name_institution Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=255)

    

class GetCampus(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
    # address_uuid: UUID | None = Field(description='Address_uuid Documentar')
    course_uuid: str | None = Field(description='Course_uuid Documentar')
    name_institution: str | None = Field(description='Name_institution Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=255)
    _normalize_nome = validator("name", allow_reuse=True)(util.normalize_lower)
    _normalize_nome = validator("name_institution", allow_reuse=True)(util.normalize_lower)
    _normalize_nome = validator("type_institution", allow_reuse=True)(util.normalize_lower)


    class Config:
        orm_mode = True



class PutCampus(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
    address_uuid: UUID | None = Field(description='Address_uuid Documentar')
    course_uuid: UUID | None = Field(description='Course_uuid Documentar')
    name_institution: str | None = Field(description='Name_institution Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=255)


class ShowCampus(GetCampus):
    address: GetAddress

    class Config:
        orm_mode = True