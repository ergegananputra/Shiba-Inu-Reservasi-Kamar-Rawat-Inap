
from models.room_models import *

class PendinginRuangan(DBServerWrites.Base):
    __tablename__ = "pendingin_ruangan"
    __table_args__ = {'extend_existing': True}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    nama = Column(String, index=True)

    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())
