from models.room_models import *

class JenisTempatTidur(DBServerWrites.Base):
    __tablename__ = "jenis_tempat_tidur"
    __table_args__ = {'extend_existing': True}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    jenis_tempat_tidur = Column(String, index=True)
    keterangan = Column(String, index=True)

    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())