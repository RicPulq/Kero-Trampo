from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostJobsArea', 'GetJobsArea', 'PutJobsArea',]



class PostJobsArea(BaseModel):
    name: str | None = Field(description='Name Documentar', max_length=255)

    

class GetJobsArea(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Nome do ramo que já trabalhou', max_length=255)

    class Config:
        orm_mode = True



class PutJobsArea(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
