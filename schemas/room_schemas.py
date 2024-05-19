'''
This file contains Pydantic models.
If you looking for SQLAlchemy models, you can find it in models/room_models.py
'''

from datetime import datetime
from pydantic import BaseModel
from typing import Optional
import uuid

class Timestamps():
    create_at: Optional[datetime] = None
    update_at: Optional[datetime] = None

class FasilitasLayananKesehatanBase(BaseModel, Timestamps):
    nama: str
    alamat: str

class FasilitasLayananKesehatanCreate(FasilitasLayananKesehatanBase):
    pass

class FasilitasLayananKesehatan(FasilitasLayananKesehatanBase):
    id: Optional[uuid.UUID] = None

    class Config:
        orm_mode = True