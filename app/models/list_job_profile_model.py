from app import db

class ListJobProfile(db.Base):

    company_uuid = db.Column(db.UUID, nullable=False)

    # UUID do perfil do trabalho
    job_profile_uuid = db.Column(db.UUID, nullable=False)
