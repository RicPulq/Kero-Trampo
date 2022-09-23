from app import db

class Pcd(db.Base):

    #nome PCD
    name = db.Column(db.String(255), nullable=False)

    #possível variável:
    # pdc_description = db.Column(db.String(255), nullable=False) 