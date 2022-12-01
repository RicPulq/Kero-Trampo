from app import db


class Students(db.Base):

    # tmax 255, campo obrigatório, Nome do Aluno
    name = db.Column(db.String(255), nullable=False)

    # tmax 255, campo obrigatório, Email do Aluno
    email = db.Column(db.String(255), nullable=False)

    # tmax 10, campo obrigatório, Data de Nascimento
    birthdate = db.Column(db.DateTime, nullable=False)

    # tmax 45, campo obrigatório, Estado Civil
    marital_status = db.Column(db.String(45), nullable=False)

    # tmax 15, campo não obrigatório, Telefone
    phone_number = db.Column(db.String(255), nullable=True)

    # tmax 15, campo não obrigatório, Disponibilidade
    availability = db.Column(db.String(15), nullable=False)

    # booleano, PCD ou não:
    pcd = db.Column(db.Boolean)

    # uuid do Usuário o qual pertence o perfil
    user_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("user.uuid"), nullable=False
    )
    user = db.relationship(
        "User", back_populates="students_relation", lazy="joined", cascade="save-update"
    )

    # uuid do Endereço o qual pertence o perfil
    address_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("address.uuid"), nullable=False
    )
    address = db.relationship(
        "Address",
        back_populates="relation_students",
        lazy="joined",
        cascade="all, delete",
    )

    # uuid do Perfil Academico do usuário que for agressista
    academic_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("academicprofiles.uuid"), nullable=False
    )
    academicprofiles = db.relationship(
        "AcademicProfiles",
        back_populates="students",
        lazy="joined",
        cascade="all, delete",
    )
    quiz = db.relationship(
        "Quiz", back_populates="student", lazy="joined", cascade="all, delete"
    )
    list_jobsarea = db.relationship(
        "ListJobsArea", back_populates="student", cascade="all, delete"
    )
    list_previouslyjobs = db.relationship(
        "ListPreviouslyJobs", back_populates="student", cascade="all, delete"
    )
    students_pcd = db.relationship(
        "StudentsPcd", back_populates="students", cascade="all, delete"
    )
