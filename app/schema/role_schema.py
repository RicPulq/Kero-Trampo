from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostRole', 'GetRole', 'PutRole',]



class PostRole(BaseModel):
    name: str | None = Field(description='Name Documentar', max_length=None)
    permission_level: int | None = Field(description='Permission_level Documentar')

    

class GetRole(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=None)
    permission_level: int | None = Field(description='Permission_level Documentar')


    class Config:
        orm_mode = True



class PutRole(BaseModel):

    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    name: str | None = Field(description='Name Documentar', max_length=None)
    permission_level: int | None = Field(description='Permission_level Documentar')
