from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from app.schema.address_schema import GetAddress

__all__ = ['PostCompany', 'GetCompany', 'PutCompany','ShowCompany']



class PostCompany(BaseModel):
    name: str | None = Field(description='Name Documentar', max_length=255)
    number_employers: int | None = Field(description='Number_employers Documentar')
    opening_hours: datetime | None = Field(description='Opening_hours Documentar')
    work_style: int | None = Field(description='Work_style Documentar')
    pcd: bool | None = Field(description='Pcd Documentar')
    link_site: str | None = Field(description='Link_site Documentar', max_length=255)
    email: str | None = Field(description='Email Documentar', max_length=255)
    phone_number: str | None = Field(description='Phone_number Documentar', max_length=255)
    # user_uuid: UUID | None = Field(description='User_uuid Documentar')
    
    

class GetCompany(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
    number_employers: int | None = Field(description='Number_employers Documentar')
    opening_hours: datetime | None = Field(description='Opening_hours Documentar')
    work_style: int | None = Field(description='Work_style Documentar')
    pcd: bool | None = Field(description='Pcd Documentar')
    link_site: str | None = Field(description='Link_site Documentar', max_length=255)
    email: str | None = Field(description='Email Documentar', max_length=255)
    phone_number: str | None = Field(description='Phone_number Documentar', max_length=255)


    class Config:
        orm_mode = True


class ShowCompany(GetCompany):
    address: GetAddress

    class Config:
        orm_mode = True



class PutCompany(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
    number_employers: int | None = Field(description='Number_employers Documentar')
    opening_hours: datetime | None = Field(description='Opening_hours Documentar')
    work_style: int | None = Field(description='Work_style Documentar')
    pcd: bool | None = Field(description='Pcd Documentar')
    link_site: str | None = Field(description='Link_site Documentar', max_length=255)
    email: str | None = Field(description='Email Documentar', max_length=255)
    phone_number: str | None = Field(description='Phone_number Documentar', max_length=255)
