"""
Database Setup.
Author: ninz
Setup database functions and make sure all db models have proper porting
to desired database.
"""
from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Tuple

from backend.config import get_config


def create_session() -> Tuple:
    """
    Creates db session and return session

    :return:
    :rtype:
    """
    config = get_config()

    _engine = create_engine(
        config.sqlalchemy_database_url, connect_args={"check_same_thread": False}
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=_engine), _engine


# Db dependency, get db
def get_db(request: Request):
    return request.state.db


Base = declarative_base()
SessionLocal, engine = create_session()
