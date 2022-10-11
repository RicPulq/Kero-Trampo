from app import db


class Courses(db.Base):

    name = db.Column(db.String(255), nullable=False)

    modality = db.Column(db.String(255), nullable=False)

    annual_graduates = db.Column(db.Integer, nullable=True)

    pcd = db.Column(db.Boolean)

    employability_index = db.Column(db.Integer, nullable=True)

    businessperson_index = db.Column(db.Integer, nullable=True)

    public_server_index = db.Column(db.Integer, nullable=True)

    # tmax 255, link do site da empresa (se tiver)
    link_site = db.Column(db.String(255), nullable=True)

    # tmax 255, email da empresa (se tiver)
    email = db.Column(db.String(255), nullable=False)

    # tmax 255, número telefonico (se tiver)
    phone_number = db.Column(db.String(255), nullable=False)

    user_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("user.uuid"), nullable=False
    )

    user = db.relationship("User", back_populates="courses_relation", lazy="joined", cascade="save-update")

    campus_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("campus.uuid"), nullable=False
    )

    campus = db.relationship("Campus", back_populates="courses", lazy="joined", cascade="all, delete")

    coursespcd = db.relationship("CoursesPCD", back_populates="courses", lazy="joined", cascade="save-update")