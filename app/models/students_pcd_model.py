from app import db

class StudentsPcd(db.Base):

    students_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("students.uuid"), nullable=False)

    pcd_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("pcd.uuid"), nullable=False)
 
    pcd = db.relationship("Pcd", back_populates="students_pcd", cascade="save-update", lazy="joined")

    students = db.relationship("Students", back_populates="students_pcd", cascade="save-update", lazy=False)

    others = db.Column(db.String(255), nullable=True)