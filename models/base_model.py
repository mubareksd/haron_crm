import models
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        if kwargs:
            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now(timezone.utc)
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now(timezone.utc)
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)

    def bm_update(self, **kwargs):
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
        self.save()

    def save(self):
        self.updated_at = datetime.now(timezone.utc)
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)



