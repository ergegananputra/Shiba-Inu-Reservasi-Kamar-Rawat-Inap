from schemas.room_schemas import *

class UsersBase(BaseModel, Timestamps):
    username: str
    password: str

class UserLogin(UsersBase):
    username: str
    password: str


class UsersCreate(UsersBase):
    pass

class Users(UsersBase):
    id: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True


