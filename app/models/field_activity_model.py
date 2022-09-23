from app import db

class FieldActivity(db.Base):

    # Ramo de atividade da empresa
    activity = db.Column(db.String(255), nullable=False)