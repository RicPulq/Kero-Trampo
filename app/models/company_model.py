from app import db


class Company(db.Base):

    # tmax 255, Nome da empresa
    name = db.Column(db.String(255), nullable=False)

    # Número de funcionários
    number_employers = db.Column(db.Integer)

    # Horário de funcionamento
    opening_hours = db.Column(db.DateTime)

    # Estilo do emprego, 1=HomeOffice, 2=Presencial, 3=Híbrido
    work_style = db.Column(db.Integer)

    # Está contratando?, True or False
    hiring = db.Column(db.Boolean)

    # PCD sim ou não
    pcd = db.Column(db.Boolean)

    # tmax 255, link do site da empresa (se tiver)
    link_site = db.Column(db.String(255), nullable=True)

    # tmax 255, email da empresa (se tiver)
    email = db.Column(db.String(255), nullable=False)

    # tmax 255, número telefonico (se tiver)
    phone_number = db.Column(db.String(255), nullable=False)

    # uuid do Usuário o qual pertence o perfil
    user_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("user.uuid"), nullable=False
    )
    user = db.relationship(
        "User", back_populates="company_relation", lazy="joined", cascade="save-update"
    )

    address_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("address.uuid"), nullable=False
    )
    address = db.relationship(
        "Address", back_populates="company", lazy="joined", cascade="all,delete"
    )
    branch = db.relationship(
        "BranchOffice", back_populates="company", cascade="all, delete"
    )
    company_pcd = db.relationship(
        "CompanyPcd", back_populates="company", cascade="save-update"
    )
    list_characteristic = db.relationship(
        "ListCharacteristics", back_populates="company", cascade="save-update"
    )
    list_hiring_problems = db.relationship(
        "ListHiringProblems", back_populates="company", cascade="save-update"
    )
    list_job_profile = db.relationship(
        "ListJobProfile", back_populates="company", cascade="save-update"
    )
