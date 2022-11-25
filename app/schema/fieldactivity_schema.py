from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostFieldActivity', 'GetFieldActivity', 'PutFieldActivity',]



class PostFieldActivity(BaseModel):
    activity: UUID | None = Field(description='Activity Documentar')

    

class GetFieldActivity(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    activity: str | None = Field(description='Activity Documentar', max_length=255)


    class Config:
        orm_mode = True



class PutFieldActivity(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    activity: str | None = Field(description='Activity Documentar', max_length=255)
