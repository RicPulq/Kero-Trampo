from app import db

class StudentsPcd(db.Base):

    students_uuid = db.Column(db.UUID, nullable=False)

    pcd_uuid = db.Column(db.UUID, nullable=False)
 