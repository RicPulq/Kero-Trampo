from app import db

class ListHiringProblems(db.Base):

    # UUID da empresa/companhia
    company_uuid = db.Column(db.UUID, nullable=False)

    # UUID do problema de contratação da empresa
    problem_uuid = db.Column(db.UUID, nullable=False)
