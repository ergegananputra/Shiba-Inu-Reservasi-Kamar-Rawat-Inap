from schemas.room_schemas import *

class JenisTempatTidurBase(BaseModel, Timestamps):
    jenis_tempat_tidur: str
    keterangan: str

class JenisTempatTidurCreate(JenisTempatTidurBase):
    pass

class JenisTempatTidur(JenisTempatTidurBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True
