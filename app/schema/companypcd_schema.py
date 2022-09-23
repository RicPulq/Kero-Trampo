from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostCompanyPcd', 'GetCompanyPcd', 'PutCompanyPcd',]



class PostCompanyPcd(BaseModel):
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    pcd_uuid: str | None = Field(description='Pcd_uuid Documentar')

    

class GetCompanyPcd(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    pcd_uuid: str | None = Field(description='Pcd_uuid Documentar')


    class Config:
        orm_mode = True



class PutCompanyPcd(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    pcd_uuid: str | None = Field(description='Pcd_uuid Documentar')
