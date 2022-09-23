from app import db

class ListFieldActivities(db.Base):

    # UUID da empresa
    company_uuid = db.Column(db.UUID, nullable=False)

    # UUID do ramo de atividade da empresa
    activity_uuid = db.Column(db.UUID, nullable=False)
