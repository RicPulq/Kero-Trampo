from app import db


class ListFieldActivities(db.Base):

    # UUID da empresa
    company_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("company.uuid"), nullable=False
    )

    # UUID do ramo de atividade da empresa
    field_activity_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("fieldactivity.uuid"), nullable=False
    )
    others = db.Column(db.String(255), nullable=True)
