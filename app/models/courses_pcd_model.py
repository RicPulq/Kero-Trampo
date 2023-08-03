from app import db

class CoursesPCD(db.Base):

    courses_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("courses.uuid"), nullable=False)

    pcd_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("pcd.uuid"), nullable=False)

    others = db.Column(db.String(255), nullable=True)

    pcd = db.relationship("Pcd", back_populates="courses_pcd", lazy="joined", cascade="save-update")

    courses = db.relationship("Courses", back_populates="coursespcd", lazy="joined", cascade="save-update")

    others = db.Column(db.String(255), nullable=True)