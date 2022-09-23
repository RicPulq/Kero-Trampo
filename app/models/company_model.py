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