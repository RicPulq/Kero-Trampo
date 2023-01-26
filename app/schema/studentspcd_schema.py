from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from app.schema.pcd_schema import GetPcd
from app.schema.students_schema import GetStudents

__all__ = ['PostStudentsPcd', 'GetStudentsPcd', 'PutStudentsPcd','ShowPCDs']



class PostStudentsPcd(BaseModel):
    students_uuid: UUID | None = Field(description='Students_uuid Documentar')
    pcd_uuid: UUID | None = Field(description='Pcd_uuid Documentar')
    class Config:
        schema_extra = {
            "example": {
                "pcd_uuid": "8c4f45a4-ddea-4c53-a325-83bc95701f29",
                "others": ""
            }
        }

    

class GetStudentsPcd(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    students_uuid: UUID | None = Field(description='Students_uuid Documentar')
    pcd_uuid: UUID | None = Field(description='Pcd_uuid Documentar')


    class Config:
        orm_mode = True


class ShowPCDs(GetStudentsPcd):
    pcd: GetPcd
    class Config:
        orm_mode=True


class PutStudentsPcd(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    # students_uuid: UUID | None = Field(description='Students_uuid Documentar')
    pcd_uuid: UUID | None = Field(description='Pcd_uuid Documentar')
