import uuid
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.exc import SQLAlchemyError
from .session import Session


def generate_uuid():
    return str(uuid.uuid4())


@as_declarative()
class Base:
    __name__: str
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    creat_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updat_at = Column(DateTime, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def create(self):
        try:
            _db = Session()
            data = self
            _db.add(data)
            _db.commit()
            _db.refresh(data)
        finally:
            _db.close()
        return data

    @classmethod
    def get(self, uuid):
        try:
            _db = Session()
            data = _db.query(self).filter_by(uuid=uuid).first()
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "dado não encontrado"}]
                )
        finally:
            _db.close()

        return data

    @classmethod
    def get_all(self):
        try:
            _db = Session()
            data = _db.query(self).all()

        finally:
            _db.close()

        return data
    
    @classmethod
    def get_paginate(self, page: int, per_page: int ):
        try:
            _offset = page* per_page
            _db = Session()
            data = _db.query(self).offset(_offset).limit(per_page).all()
        finally:
            _db.close()
        return data

    @classmethod
    def remove(self, uuid):
        try:
            _db = Session()
            data = _db.query(self).filter_by(uuid=uuid).first()
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "dado não encontrado"}]
                )
            _db.delete(data)
            _db.commit()
        except:
            _db.rollback()
        finally:
            _db.close()

        return "OK"

    def flush(self):
        try:
            _db = Session()
            _db.add(self)
            _db.flush()
            _db.close()
        except:
            _db.rollback()

        finally:
            _db.close()

        return True

    @classmethod
    def update(self, uuid, **request_data):
        try:
            _db = Session()
            data = _db.query(self).filter_by(uuid=uuid).first()
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "Dado não encontrado"}]
                )
            for key, value in request_data.items():
                setattr(data, key, value)
            _db.add(data)
            _db.commit()
            _db.refresh(data)
        except:
            _db.rollback()
        finally:
            _db.close()

        return data

    @classmethod
    def exist(self,args, kargs):
        try:
            _db = Session()
            # data = _db.query(self).filter_by(username=args).first()
            data = _db.query(self).filter(getattr(self,args)== kargs).first()
                
        finally:
            _db.close()
        return data


    @classmethod
    def get_dict(self, kwargs):
        try:
            _db = Session()
            data = _db.query(self)
            for k, v in kwargs.items():
                if v is not None:
                    data = data.filter(getattr(self, k) == v)
            data = data.all()
        except:
            _db.rollback()
        finally:
            _db.close()
        return data

    @classmethod
    def get_list(self, kwargs):
        try:
            kwargs = list(kwargs.items())
            _db = Session()
            data = _db.query(self).filter(getattr((self), kwargs[0][0]) == kwargs[0][1])
            for li in kwargs[1:]:
                data = data.filter(getattr((self), li[0]) == li[1])
        except:
            _db.rollback()
        finally:
            _db.close()
