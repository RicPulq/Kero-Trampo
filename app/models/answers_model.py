from app import db

class Answers(db.Base):

    #tmax 255, campo obrigatório, Respostas
    answer = db.Column(db.String(255), unique=True, nullable=False)

    #boolean, Resposta do tipo booleano
    bool_answer = db.Column(db.Boolean)

    quiz = db.relationship("Quiz", back_populates="answers", lazy="joined", cascade="save-update")