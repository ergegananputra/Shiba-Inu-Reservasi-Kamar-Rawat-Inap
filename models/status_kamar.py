from models.room_models import *


class StatusKamar(DBServerWrites.Base):
    __tablename__ = "status_kamar"
    __table_args__ = {'extend_existing': True}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    status = Column(String, index=True)

    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())