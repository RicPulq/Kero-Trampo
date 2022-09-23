from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostCampus', 'GetCampus', 'PutCampus',]



class PostCampus(BaseModel):
    name: str | None = Field(description='Name Documentar', max_length=255)
    address_uuid: str | None = Field(description='Address_uuid Documentar')
    course_uuid: str | None = Field(description='Course_uuid Documentar')
    name_institution: str | None = Field(description='Name_institution Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=255)

    

class GetCampus(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
    address_uuid: str | None = Field(description='Address_uuid Documentar')
    course_uuid: str | None = Field(description='Course_uuid Documentar')
    name_institution: str | None = Field(description='Name_institution Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=255)


    class Config:
        orm_mode = True



class PutCampus(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
    address_uuid: str | None = Field(description='Address_uuid Documentar')
    course_uuid: str | None = Field(description='Course_uuid Documentar')
    name_institution: str | None = Field(description='Name_institution Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=255)
