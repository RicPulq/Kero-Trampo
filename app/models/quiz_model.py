from app import db


class Quiz(db.Base):

    #uuid, campo obrigatório, Id do Aluno que Respondeu
    students_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("students.uuid"), nullable=False
    )

    #uuid, campo obrigatório, Id da Questão
    questions_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("questions.uuid"), nullable=False
    )

    #uuid, campo obrigatório, Id da Resposta
    answers_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("answers.uuid"), nullable=True)

    others = db.Column(db.String(255), nullable=True)

    student = db.relationship("Students", back_populates="quiz", lazy="joined", cascade="save-update")

    questions = db.relationship("Questions", back_populates="quiz", lazy="joined", cascade="save-update")

    answers = db.relationship("Answers", back_populates="quiz", lazy="joined", cascade="save-update")