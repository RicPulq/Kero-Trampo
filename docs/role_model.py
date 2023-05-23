from app import db


class Role(db.Base):
    
    name = db.Column(db.String(), nullable=False)
    permission_level = db.Column(db.Integer())
    