from schemas.room_schemas import *

class FasilitasLayananKesehatanBase(BaseModel, Timestamps):
    nama: str
    alamat: str

class FasilitasLayananKesehatanCreate(FasilitasLayananKesehatanBase):
    pass

class FasilitasLayananKesehatan(FasilitasLayananKesehatanBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True