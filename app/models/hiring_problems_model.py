from app import db

class HiringProblems(db.Base):

    # Nome/Qual é o problema
    problem = db.Column(db.String(255), unique=True, nullable=False)

    list = db.relationship("ListHiringProblems", back_populates="hiring_problems", cascade="save-update")