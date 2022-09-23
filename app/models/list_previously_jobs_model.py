from app import db

class ListPreviouslyJobs(db.Base):
    student_uuid = db.Column(db.UUID, nullable=False)
    prev_job_uuid = db.Column(db.UUID, nullable=False)
