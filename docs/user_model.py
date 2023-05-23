from fastapi import HTTPException
from sqlalchemy import false

from app import db, core


class User(db.Base):

    username= db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)

    
    @classmethod
    def login(self, username: str, password: str):
        try:
            _db = db.Session()
            data = _db.query(self).filter_by(username=username).first()
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "Usuario ou senha invalidos"}]
                )

            if not data.active:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "Usuario Inativo"}]
                )
            if not core.verify_password(password, data.password):
                raise HTTPException(
                    status_code=404, detail=[{"msg": "Usuario ou senha invalidos"}]
                )
        finally:
            _db.close()

        return data