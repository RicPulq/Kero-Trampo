from app import db

class Answers(db.Base):

    #tmax 255, campo obrigatório, Respostas
    answer = db.Column(db.String(255), nullable=False)

    #boolean, Resposta do tipo booleano
    bool_answer = db.Column(db.Boolean)