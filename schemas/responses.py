from schemas.room_schemas import *
from typing import Generic, TypeVar

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    status: str
    message: str
    data: Optional[T] = None

    class Config:
        from_attributes = True