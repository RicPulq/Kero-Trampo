from app import db


class Address(db.Base):
    # tmax 255, campo nao obrigatorio, Nome da Rua
    street = db.Column(db.String(255), nullable=True)

    # tmax 15, , campo nao obrigatorio,, Número do endereço de contato do comprador.
    number = db.Column(db.String(15), nullable=True)

    # tmax 50, nao, Complemento do endereço de contato do comprador
    complement = db.Column(db.String(50), nullable=True)

    # tmax 50, nao, Cidade do endereço de contato do compradorz.
    city = db.Column(db.String(50), nullable=True)

    # tmax 2, nao, Estado do endereço de contato do comprador.
    state = db.Column(db.String(2), nullable=True)

    # tmax 35, nao, País do endereço de contato do comprador.
    country = db.Column(db.String(35), nullable=True)

    # tmax 50, nao, Bairro do endereço de contato do comprador.
    district = db.Column(db.String(50), nullable=True)

    # tmax 8, CEP
    cep = db.Column(db.String(8), nullable=True)

    relation_students = db.relationship(
        "Students", back_populates="address", cascade="save-update"
    )
    campus = db.relationship(
        "Campus", back_populates="address", cascade="save-update"
    )
    company = db.relationship(
        "Company", back_populates="address", cascade="save-update"
    )
    branch = db.relationship(
        "BranchOffice", back_populates="address", cascade="save-update"
    )
