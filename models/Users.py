from models.room_models import *



class User(DBServerWrites.Base):
    __tablename__ = "users"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())