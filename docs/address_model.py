from app import db


class Address(db.Base):

    # tmax 255, campo nao obrigatorio, Nome da Rua
    street = db.Column(db.String(255), nullable=True)

    # tmax 15, , campo nao obrigatorio,, Número do endereço de contato do comprador.
    number= db.Column(db.String(15), nullable=True)

    # tmax 50, nao, Complemento do endereço de contato do comprador
    complement= db.Column(db.String(50), nullable=True)

    # tmax 9, nao, CEP do endereço de contato do comprador.
    zipCode= db.Column(db.String(9), nullable=True)

    # tmax 50, nao, Cidade do endereço de contato do comprador.
    city= db.Column(db.String(50), nullable=True)

    # tmax 2, nao, Estado do endereço de contato do comprador.
    state= db.Column(db.String(2), nullable=True)

    # tmax 35, nao, País do endereço de contato do comprador.
    country= db.Column(db.String(35), nullable=True)

    # tmax 50, nao, Bairro do endereço de contato do comprador.
    district= db.Column(db.String(50), nullable=True)

    # tmax 15, nao, distância ao Equador medida ao longo do meridiano de Greenwich.
    lat = db.Column(db.String(15), nullable=True)

    # tmax 15, nao, distância ao meridiano de Greenwich medida ao longo do Equador..
    lon= db.Column(db.String(15), nullable=True)

    user_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("user.uuid"), nullable=True
    )