from app import db

class ListJobsArea(db.Base):

    # UUID do estudante
    student_uuid = db.Column(db.UUID, nullable=False)

    # UUID da área de trabalho
    jobs_area_uuid = db.Column(db.UUID, nullable=False)