from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostStudentsPcd', 'GetStudentsPcd', 'PutStudentsPcd',]



class PostStudentsPcd(BaseModel):
    students_uuid: str | None = Field(description='Students_uuid Documentar')
    pcd_uuid: str | None = Field(description='Pcd_uuid Documentar')

    

class GetStudentsPcd(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    students_uuid: str | None = Field(description='Students_uuid Documentar')
    pcd_uuid: str | None = Field(description='Pcd_uuid Documentar')


    class Config:
        orm_mode = True



class PutStudentsPcd(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    students_uuid: str | None = Field(description='Students_uuid Documentar')
    pcd_uuid: str | None = Field(description='Pcd_uuid Documentar')
