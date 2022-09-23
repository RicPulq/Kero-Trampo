from app import db

class BranchOffice(db.Base):

    company_uuid = db.Column(db.UUID, nullable=False)

    # Nome da filial
    name = db.Column(db.String(255), nullable=False)

    address_uuid = db.Column(db.UUID, nullable=False)
