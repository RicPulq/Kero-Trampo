from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostListCharacteristics', 'GetListCharacteristics', 'PutListCharacteristics',]



class PostListCharacteristics(BaseModel):
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    characteristic_uuid: str | None = Field(description='Characteristic_uuid Documentar')

    

class GetListCharacteristics(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    characteristic_uuid: str | None = Field(description='Characteristic_uuid Documentar')


    class Config:
        orm_mode = True



class PutListCharacteristics(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    characteristic_uuid: str | None = Field(description='Characteristic_uuid Documentar')
