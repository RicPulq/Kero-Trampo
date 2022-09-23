from unicodedata import name
from app import db

class Campus(db.Base):

    name = db.Column(db.String(255), nullable = False)

    address_uuid = db.Column(db.UUID, nullable = False)

    course_uuid = db.Column(db.UUID, nullable = False)

    name_institution = db.Column(db.String(255), nullable = False)

    type_institution = db.Column(db.String(255), nullable = False)