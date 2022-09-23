from app import db 

class JobsArea(db.Base):

    #tmax 255, campo obrigatório, Área de Trabalho
    name = db.Column(db.String(255), nullable=False)