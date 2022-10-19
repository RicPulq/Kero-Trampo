from app import db


class ListJobProfile(db.Base):

    company_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("company.uuid"), nullable=False
    )

    # UUID do perfil do trabalho
    job_profile_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("jobsprofile.uuid"), nullable=False
    )
    others = db.Column(db.String(255), nullable=True)

    job_profile = db.relationship(
        "JobsProfile", back_populates="list", cascade="save-update", lazy="joined"
    )

    company = db.relationship(
        "Company",
        back_populates="list_job_profile",
        cascade="save-update",
        lazy="joined",
    )
