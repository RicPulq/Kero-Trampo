from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostPreviouslyJob', 'GetPreviouslyJob', 'PutPreviouslyJob',]



class PostPreviouslyJob(BaseModel):
    name: str | None = Field(description='Name Documentar', max_length=255)

    

class GetPreviouslyJob(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)


    class Config:
        orm_mode = True



class PutPreviouslyJob(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=255)
