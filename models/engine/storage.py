from dotenv import load_dotenv
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base
from models.swift_request import SwiftRequest

load_dotenv()

MYSQL_USER = environ.get('MYSQL_USER')
MYSQL_PWD = environ.get('MYSQL_PWD')
MYSQL_HOST = environ.get('MYSQL_HOST')
MYSQL_DB = environ.get('MYSQL_DB')


class Storage:
    __engine = None
    __session = None

    CNC = {
        'SwiftRequest': SwiftRequest
    }

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB)
        )

    def all(self, cls=None):
        if cls:
            return self.__session.query(Storage.CNC[cls]).all()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )

    def close(self):
        self.__session.remove()

    def get(self, cls, id):
        if cls and id:
            return self.__session.query(Storage.CNC[cls]).get(id)
        return None

    def count(self, cls=None):
        if cls:
            return self.__session.query(Storage.CNC[cls]).count()
        return None
