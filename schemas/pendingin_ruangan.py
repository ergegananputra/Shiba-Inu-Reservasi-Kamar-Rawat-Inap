from schemas.room_schemas import *

class PendinginRuanganBase(BaseModel, Timestamps):
    nama: str

class PendinginRuanganCreate(PendinginRuanganBase):
    pass

class PendinginRuangan(PendinginRuanganBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True