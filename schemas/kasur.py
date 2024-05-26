from schemas.room_schemas import *

class KasurBase(BaseModel, Timestamps):
    fk_fkr: uuid.UUID
    fk_sk: uuid.UUID
    fk_jtt: uuid.UUID
    fk_fdk: uuid.UUID
    tingkat_fasilitas_kesehatan: str
    biaya_pakai_per_hari: float
    kode_kamar: str

class KasurCreate(KasurBase):
    pass

class Kasur(KasurBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True
