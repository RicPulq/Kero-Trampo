from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostListJobProfile', 'GetListJobProfile', 'PutListJobProfile',]



class PostListJobProfile(BaseModel):
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    job_profile_uuid: str | None = Field(description='Job_profile_uuid Documentar')

    

class GetListJobProfile(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    job_profile_uuid: str | None = Field(description='Job_profile_uuid Documentar')


    class Config:
        orm_mode = True



class PutListJobProfile(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    job_profile_uuid: str | None = Field(description='Job_profile_uuid Documentar')
