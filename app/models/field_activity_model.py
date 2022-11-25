from app import db

class FieldActivity(db.Base):

    # Ramo de atividade da empresa
    activity = db.Column(db.String(255), nullable=False)

    list = db.relationship("ListFieldActivities", back_populates="field_activity", cascade="save-update", lazy="joined")