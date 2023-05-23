from fastapi import HTTPException
from app import db, core
from app.core.security import get_password_hash


class User(db.Base):
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    role_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("role.uuid"), nullable=False
    )
    students_relation = db.relationship(
        "Students", back_populates="user", lazy="joined", cascade="all, delete"
    )
    company_relation = db.relationship(
        "Company", back_populates="user", lazy="joined", cascade="all,delete"
    )
    courses_relation = db.relationship(
        "Courses", back_populates="user", lazy="joined", cascade="all,delete"
    )
    role = db.relationship("Role", back_populates="user", cascade="save-update", lazy="joined")

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
