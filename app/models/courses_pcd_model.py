from app import db

class CoursesPCD(db.Base):

    courses_uuid = db.Column(db.UUID, nullable=False)

    pcd_uuid = db.Column(db.UUID, nullable=False)
 