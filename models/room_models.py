'''
This file contains SQLAlchemy models. 
If you looking for Pydantic models, you can find it in schemas/room_schemas.py

'''

import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import uuid

from database.database import DBServerWrites

class FasilitasLayananKesehatan(DBServerWrites.Base):
    __tablename__ = "fasilitas_layanan_kesehatan"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    nama = Column(String, index=True)
    alamat = Column(String, index=True)
    tipe = Column(String, index=True)
    
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())
