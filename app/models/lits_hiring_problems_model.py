from app import db


class ListHiringProblems(db.Base):

    # UUID da empresa/companhia
    company_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("company.uuid"), nullable=False
    )

    # UUID do problema de contratação da empresa
    hiring_problems_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("hiringproblems.uuid"), nullable=False
    )
    others = db.Column(db.String(255), nullable=True)

    hiring_problems = db.relationship(
        "HiringProblems", back_populates="list", cascade="save-update", lazy="joined"
    )

    company = db.relationship(
        "Company",
        back_populates="list_hiring_problems",
        cascade="save-update",
        lazy="joined",
    )
