from unicodedata import name
from app import db

class Campus(db.Base):

    name = db.Column(db.String(255), nullable = False)

    address_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("address.uuid"), nullable = False)

    name_institution = db.Column(db.String(255), nullable = False)

    type_institution = db.Column(db.String(255), nullable = False)

    courses = db.relationship("Courses", back_populates="campus", lazy="joined", cascade="save-update")

    address = db.relationship("Address", back_populates="campus", lazy="joined", cascade="all, delete")