from app import db

class EmployerCharacteristics(db.Base):

    # tmax 255, Caracteristica
    characteristc = db.Column(db.String(255), nullable=False)

    list = db.relationship("ListCharacteristics", back_populates="employercharacteristics", cascade="save-update")