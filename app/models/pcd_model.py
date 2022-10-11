from app import db

class Pcd(db.Base):

    #nome PCD
    name = db.Column(db.String(255), nullable=False)

    courses_pcd = db.relationship("CoursesPCD", back_populates="pcd", lazy="joined", cascade="save-update")
    #possível variável:
    # pdc_description = db.Column(db.String(255), nullable=False) 