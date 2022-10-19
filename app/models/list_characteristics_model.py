from app import db


class ListCharacteristics(db.Base):

    # UUID da empresa
    company_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("company.uuid"), nullable=False
    )

    # UUID da caracteristica de funcionario desejada
    characteristic_uuid = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("employercharacteristics.uuid"),
        nullable=False,
    )
    others = db.Column(db.String(255), nullable=True)

    employercharacteristics = db.relationship(
        "EmployerCharacteristics",
        back_populates="list",
        cascade="save-update",
        lazy="joined",
    )

    company = db.relationship(
        "Company",
        back_populates="list_characteristic",
        cascade="save-update",
        lazy="joined",
    )
