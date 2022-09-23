from app import db


class Profile(db.Base):

    # tmax 255, sim, Nome do comprador.
    name = db.Column(db.String(255), nullable=True)
    # tmax 14, sim, Número do CPF ou CNPJ do cliente.
    identity = db.Column(db.String(14), nullable=True)
    # tmax 255, sim, Tipo de documento de identificação do comprador (CPF ou CNPJ).
    identity_type= db.Column(db.String(255), nullable=True)
    # tmax 10, nao, Data de nascimento do comprador no formato AAAA-MM-DD.
    birthdate= db.Column(db.String(10), nullable=True)
    # tmax 45, nao, Endereço de IP do comprador. Suporte a IPv4 e IPv6.
    ip_address= db.Column(db.String(45), nullable=True)


    user_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("user.uuid"), nullable=True
    )