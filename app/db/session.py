import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import core

engine = create_engine(core.settings.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
