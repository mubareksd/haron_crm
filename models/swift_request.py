from sqlalchemy import Column, String

from models.base_model import Base, BaseModel


class SwiftRequest(BaseModel, Base):
    __tablename__ = 'swift_requests'
    business_name = Column(String(60), nullable=False)
    contact_name = Column(String(60), nullable=False)
    contact_email = Column(String(60), nullable=False)
    contact_phone = Column(String(60), nullable=False)
    contact_address = Column(String(60), nullable=False)
    contact_city = Column(String(60), nullable=False)
    contact_state = Column(String(60), nullable=False)
    contact_zip = Column(String(60), nullable=False)
    contact_country = Column(String(60), nullable=False)
    status = Column(String(60), nullable=False, default='Pending')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
