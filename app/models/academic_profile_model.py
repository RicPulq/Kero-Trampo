from app import db


class AcademicProfiles(db.Base):
    # Perfil Acadêmico do Aluno Egressante

    # tmax 255, campo obrigátorio, Nome da Instituição de Ensino
    education_instution = db.Column(db.String(255), nullable=False)

    # tmax 255, campo obrigátorio, Nome do Campus
    campus_name = db.Column(db.String(255), nullable=False)

    # tmax 255, campo obrigatório, Cidade onde fica a Instituição
    city_instution = db.Column(db.String(255), nullable=False)

    # tmax 255, campo obrigatório, Nome do Curso realizado
    course_name = db.Column(db.String(255), nullable=False)

    # tmax 45, campo obrigatório, Tipo da Instituição (Pública ou Privada)
    type_institution = db.Column(db.String(45), nullable=False)

    # tmax 45, campo obrigatório, Modalidade de Ensino
    teaching_modality = db.Column(db.String(45), nullable=False)

    # tmax 255, campo obrigatório, Outros Curso (se já concluídos)
    other_courses = db.Column(db.String(255), nullable=False)

    # coeficiente academico, opcional
    academic_coefficient = db.Column(db.Float, nullable=True)

    students = db.relationship(
        "Students",
        back_populates="academicprofiles",
        lazy="joined",
        cascade="save-update",
    )
