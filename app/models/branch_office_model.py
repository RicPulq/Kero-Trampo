from app import db

class BranchOffice(db.Base):
    # Nome da filial
    name = db.Column(db.String(255), nullable=False)

    company_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("company.uuid"), nullable=False)

    company = db.relationship("Company", back_populates="branch", cascade="save-update", lazy="joined")

    address_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("address.uuid"), nullable=False)

    address = db.relationship("Address", back_populates="branch",lazy="joined", cascade="all, delete")