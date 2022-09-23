from app import db

class Questions(db.Base):

    #tmax 255, campo obrigatório, Perguntas
    questions = db.Column(db.String(255), nullable=False)
    