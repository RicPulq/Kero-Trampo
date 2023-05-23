from app import db

class JobsProfile(db.Base):

    #tmax 255, campo obrigatório, Perfil do Trabalho
    name = db.Column(db.String(255), nullable=False)

    list = db.relationship("ListJobProfile", back_populates="job_profile", cascade="save-update")