from schemas.room_schemas import *

class FasilitasDetailKamarBase(BaseModel, Timestamps):
    kamar_mandi: int
    tabung_oksigen: int
    infus: int
    nurse_call: int
    kasur_pendamping: int
    sofa: int
    lemari: int
    meja_makan_pasien: int
    meja_makan_pendamping: int
    televisi: int
    dispenser: int
    kulkas: int
    wastafel: int

class FasilitasDetailKamarCreate(FasilitasDetailKamarBase):
    fk_fpr: uuid.UUID
    pass

class FasilitasDetailKamar(FasilitasDetailKamarBase):
    id: Optional[uuid.UUID] = None
    fk_fpr: uuid.UUID

    class Config:
        from_attributes = True