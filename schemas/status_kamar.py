from schemas.room_schemas import *

class StatusKamarBase(BaseModel, Timestamps):
    status: str

class StatusKamarCreate(StatusKamarBase):
    pass

class StatusKamar(StatusKamarBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True