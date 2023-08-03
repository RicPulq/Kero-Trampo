from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from app.schema.company_schema import GetCompany

from app.schema.pcd_schema import GetPcd

__all__ = [
    "PostCompanyPcd",
    "GetCompanyPcd",
    "PutCompanyPcd",
    "ShowCompanyPCDs"
]


class PostCompanyPcd(BaseModel):
    # company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    pcd_uuid: UUID | None = Field(description="Pcd_uuid Documentar")
    class Config:
        schema_extra = {
            "example": {
                "pcd_uuid": "8c4f45a4-ddea-4c53-a325-83bc95701f29",
                "others": ""
            }
        }


class GetCompanyPcd(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    pcd_uuid: UUID | None = Field(description="Pcd_uuid Documentar")
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )

    class Config:
        orm_mode = True


class ShowCompanyPCDs(GetCompanyPcd):
    pcd: GetPcd
    company: GetCompany

    class Config:
        orm_mode = True


class PutCompanyPcd(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    # company_uuid: UUID | None = Field(description='Company_uuid Documentar')
    pcd_uuid: UUID | None = Field(description="Pcd_uuid Documentar")
