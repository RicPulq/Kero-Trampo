from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostEmployerCharacteristics', 'GetEmployerCharacteristics', 'PutEmployerCharacteristics',]



class PostEmployerCharacteristics(BaseModel):
    characteristc: str | None = Field(description='Characteristc Documentar', max_length=255)

    

class GetEmployerCharacteristics(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    characteristc: str | None = Field(description='Characteristc Documentar', max_length=255)


    class Config:
        orm_mode = True



class PutEmployerCharacteristics(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    characteristc: str | None = Field(description='Characteristc Documentar', max_length=255)
