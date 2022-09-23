from app import db

class ListCharacteristics(db.Base):

    # UUID da empresa
    company_uuid = db.Column(db.UUID, nullable=False)

    # UUID da caracteristica de funcionario desejada
    characteristic_uuid = db.Column(db.UUID, nullable=False)
 