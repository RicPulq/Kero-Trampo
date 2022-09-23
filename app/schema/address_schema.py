from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostAddress', 'GetAddress', 'PutAddress',]



class PostAddress(BaseModel):
    street: str | None = Field(description='Street Documentar', max_length=255)
    number: str | None = Field(description='Number Documentar', max_length=15)
    complement: str | None = Field(description='Complement Documentar', max_length=50)
    city: str | None = Field(description='City Documentar', max_length=50)
    state: str | None = Field(description='State Documentar', max_length=2)
    country: str | None = Field(description='Country Documentar', max_length=35)
    district: str | None = Field(description='District Documentar', max_length=50)

    

class GetAddress(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    street: str | None = Field(description='Street Documentar', max_length=255)
    number: str | None = Field(description='Number Documentar', max_length=15)
    complement: str | None = Field(description='Complement Documentar', max_length=50)
    city: str | None = Field(description='City Documentar', max_length=50)
    state: str | None = Field(description='State Documentar', max_length=2)
    country: str | None = Field(description='Country Documentar', max_length=35)
    district: str | None = Field(description='District Documentar', max_length=50)


    class Config:
        orm_mode = True



class PutAddress(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    street: str | None = Field(description='Street Documentar', max_length=255)
    number: str | None = Field(description='Number Documentar', max_length=15)
    complement: str | None = Field(description='Complement Documentar', max_length=50)
    city: str | None = Field(description='City Documentar', max_length=50)
    state: str | None = Field(description='State Documentar', max_length=2)
    country: str | None = Field(description='Country Documentar', max_length=35)
    district: str | None = Field(description='District Documentar', max_length=50)
