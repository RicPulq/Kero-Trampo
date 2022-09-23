from app import db


class Quiz(db.Base):

    #uuid, campo obrigatório, Id do Aluno que Respondeu
    student_uuid = db.Column(db.UUID, nullable=False)

    #uuid, campo obrigatório, Id da Questão
    question_uuid = db.Column(db.UUID, nullable=False)

    #uuid, campo obrigatório, Id da Resposta
    answer_uuid = db.Column(db.UUID, nullable=False)
 