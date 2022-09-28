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

    # address_uuid = db.Column(
    #     db.UUID(as_uuid=True), db.ForeignKey("address.uuid"), nullable=False
    # )
