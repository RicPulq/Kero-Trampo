from app import db


class CompanyPcd(db.Base):

    company_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("company.uuid"), nullable=False
    )

    pcd_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("pcd.uuid"), nullable=False
    )

    company = db.relationship(
        "Company", back_populates="company_pcd", lazy="joined", cascade="save-update"
    )

    pcd = db.relationship(
        "Pcd", back_populates="company_pcd", lazy="joined", cascade="save-update"
    )
