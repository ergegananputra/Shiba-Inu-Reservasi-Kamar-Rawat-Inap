from schemas.room_schemas import *

class FasilitasDetailKamarBase(BaseModel, Timestamps):
    fk_fpr: uuid.UUID
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
    pass

class FasilitasDetailKamar(FasilitasDetailKamarBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True