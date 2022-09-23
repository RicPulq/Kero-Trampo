from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from .students_schema import GetStudents
from .company_schema import GetCompany
from .courses_schema import GetCourses
from typing import List

__all__ = ['PostUser', 'GetUser', 'PutUser',]



class PostUser(BaseModel):
    username: str | None = Field(description='Username Documentar', max_length=255)
    password: str | None = Field(description='Password Documentar', max_length=255)
    active: bool | None = Field(description='Active Documentar')
    role_uuid: UUID | None = Field(description='Role_uuid Documentar')

    

class GetUser(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    username: str | None = Field(description='Username Documentar', max_length=255)
    password: str | None = Field(description='Password Documentar', max_length=255)
    active: bool | None = Field(description='Active Documentar')
    role_uuid: UUID | None = Field(description='Role_uuid Documentar')


    class Config:
        orm_mode = True



class ShowUser(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    username: str | None = Field(description='Username Documentar', max_length=255)
    password: str | None = Field(description='Password Documentar', max_length=255)
    active: bool | None = Field(description='Active Documentar')
    role_uuid: UUID | None = Field(description='Role_uuid Documentar')
    company_relation: List[GetCompany] = []
    students_relation: List[GetStudents] = []
    courses_relation: List[GetCourses] = []

    class Config:
        orm_mode = True



class PutUser(BaseModel):
    
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    username: str | None = Field(description='Username Documentar', max_length=255)
    password: str | None = Field(description='Password Documentar', max_length=255)
    active: bool | None = Field(description='Active Documentar')
    role_uuid: UUID | None = Field(description='Role_uuid Documentar')
