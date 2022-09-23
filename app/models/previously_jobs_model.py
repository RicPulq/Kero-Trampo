from app import db

class PreviouslyJob(db.Base):

    #tmax 255, campo obrigatório, Trabalhos Anteriores
    name = db.Column(db.String(255), nullable=False)