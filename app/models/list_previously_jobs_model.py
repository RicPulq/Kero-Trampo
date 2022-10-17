from app import db


class ListPreviouslyJobs(db.Base):
    student_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("students.uuid"), nullable=False
    )

    student = db.relationship("Students", back_populates="list_previouslyjobs",cascade="save-update", lazy="joined")

    prev_job_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("previouslyjob.uuid"), nullable=False
    )

    previouslyjob = db.relationship("PreviouslyJob", back_populates="list", cascade="save-update", lazy="joined")

    others = db.Column(db.String(255), nullable=True)
