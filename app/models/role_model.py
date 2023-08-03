from app import db


class Role(db.Base):
    
    name = db.Column(db.String(), unique=True, nullable=False)
    permission_level = db.Column(db.Integer())
    user = db.relationship("User", back_populates="role", cascade="save-update")

