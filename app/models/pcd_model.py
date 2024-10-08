from app import db


class Pcd(db.Base):

    # nome PCD
    name = db.Column(db.String(255), unique=True,nullable=False)

    students_pcd = db.relationship(
        "StudentsPcd", back_populates="pcd", cascade="save-update"
    )

    courses_pcd = db.relationship(
        "CoursesPCD", back_populates="pcd", cascade="save-update"
    )

    company_pcd = db.relationship(
        "CompanyPcd", back_populates="pcd", lazy="joined", cascade="save-update"
    )

    # possível variável:
    # pdc_description = db.Column(db.String(255), nullable=False)
