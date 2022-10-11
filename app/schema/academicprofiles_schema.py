from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostAcademicProfiles', 'GetAcademicProfiles', 'PutAcademicProfiles',]



class PostAcademicProfiles(BaseModel):
    education_instution: str | None = Field(description='Education_instution Documentar', max_length=255)
    campus_name: str | None = Field(description='Campus_name Documentar', max_length=255)
    city_instution: str | None = Field(description='City_instution Documentar', max_length=255)
    course_name: str | None = Field(description='Course_name Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=45)
    teaching_modality: str | None = Field(description='Teaching_modality Documentar', max_length=45)
    other_courses: str | None = Field(description='Other_courses Documentar', max_length=255)
    academic_coefficient: int | None = Field(description='Coeficiente Acadêmico, favor transformar em inteiro de 0 a 100')

    

class GetAcademicProfiles(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    education_instution: str | None = Field(description='Education_instution Documentar', max_length=255)
    campus_name: str | None = Field(description='Campus_name Documentar', max_length=255)
    city_instution: str | None = Field(description='City_instution Documentar', max_length=255)
    course_name: str | None = Field(description='Course_name Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=45)
    teaching_modality: str | None = Field(description='Teaching_modality Documentar', max_length=45)
    other_courses: str | None = Field(description='Other_courses Documentar', max_length=255)
    academic_coefficient: int | None = Field(description='Academic_coefficient Documentar')


    class Config:
        orm_mode = True



class PutAcademicProfiles(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    education_instution: str | None = Field(description='Education_instution Documentar', max_length=255)
    campus_name: str | None = Field(description='Campus_name Documentar', max_length=255)
    city_instution: str | None = Field(description='City_instution Documentar', max_length=255)
    course_name: str | None = Field(description='Course_name Documentar', max_length=255)
    type_institution: str | None = Field(description='Type_institution Documentar', max_length=45)
    teaching_modality: str | None = Field(description='Teaching_modality Documentar', max_length=45)
    other_courses: str | None = Field(description='Other_courses Documentar', max_length=255)
    academic_coefficient: int | None = Field(description='Academic_coefficient Documentar')
