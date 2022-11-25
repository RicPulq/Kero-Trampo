from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from app.schema.company_schema import GetCompany
from app.schema.employercharacteristics_schema import GetEmployerCharacteristics


__all__ = [
    "PostListCharacteristics",
    "GetListCharacteristics",
    "PutListCharacteristics",
    "ShowList"
]


class PostListCharacteristics(BaseModel):
    # company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    characteristic_uuid: UUID | None = Field(
        description="Characteristic_uuid Documentar"
    )
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )


class GetListCharacteristics(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    characteristic_uuid: UUID | None = Field(
        description="Characteristic_uuid Documentar"
    )
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )


    class Config:
        orm_mode = True

class ShowList(GetListCharacteristics):
    company: GetCompany
    employercharacteristics: GetEmployerCharacteristics
    class Config:
        orm_mode = True



class PutListCharacteristics(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    characteristic_uuid: UUID | None = Field(
        description="Characteristic_uuid Documentar"
    )
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )
