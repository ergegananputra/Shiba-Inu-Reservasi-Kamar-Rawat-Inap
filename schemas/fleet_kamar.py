from schemas.room_schemas import *

class FleetKamarBase(BaseModel, Timestamps):
    fk_flk: uuid.UUID
    nama: str
    jenis_kamar: str
    informasi_pembayaran: str

class FleetKamarCreate(FleetKamarBase):
    pass

class FleetKamar(FleetKamarBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True