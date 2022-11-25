from app import db


class ListFieldActivities(db.Base):

    # UUID da empresa
    company_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("company.uuid"), nullable=False
    )

    company = db.relationship(
        "Company",
        back_populates="list_field_activities",
        cascade="save-update",
        lazy="joined",
    )

    # UUID do ramo de atividade da empresa
    field_activity_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("fieldactivity.uuid"), nullable=False
    )
    field_activity = db.relationship(
        "FieldActivity", back_populates="list", cascade="save-update", lazy="joined"
    )

    others = db.Column(db.String(255), nullable=True)
