from app import db

class HiringProblems(db.Base):

    # Nome/Qual é o problema
    problem = db.Column(db.String(255), nullable=False)
