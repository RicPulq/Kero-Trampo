from app import db


class ListJobsArea(db.Base):

    # UUID do estudante
    student_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("students.uuid"), nullable=False
    )

    student = db.relationship(
        "Students", back_populates="list_jobsarea", lazy="joined",cascade="save-update"
    )

    # UUID da área de trabalho
    jobs_area_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("jobsarea.uuid"), nullable=False
    )

    jobsarea = db.relationship("JobsArea", back_populates="list", lazy="joined",cascade="save-update")

    others = db.Column(db.String(255), nullable=True)
