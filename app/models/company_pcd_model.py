from app import db

class CompanyPcd(db.Base):

    company_uuid = db.Column(db.UUID, nullable=False)

    pcd_uuid = db.Column(db.UUID, nullable=False)
 