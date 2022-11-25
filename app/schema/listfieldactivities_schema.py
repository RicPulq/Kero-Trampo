from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostListFieldActivities', 'GetListFieldActivities', 'PutListFieldActivities',]



class PostListFieldActivities(BaseModel):
    # company_uuid: str | None = Field(description='Company_uuid Documentar')
    field_activity_uuid: UUID | None = Field(description='Activity_uuid Documentar')
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )
    

class GetListFieldActivities(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    activity_uuid: str | None = Field(description='Activity_uuid Documentar')


    class Config:
        orm_mode = True



class PutListFieldActivities(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    activity_uuid: str | None = Field(description='Activity_uuid Documentar')
