from models.room_models import *

class FleetKamar(DBServerWrites.Base):
    __tablename__ = "fleet_kamar"
    __table_args__ = {'extend_existing': True}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    fk_flk = Column(UUIDType(binary=False), ForeignKey('fasilitas_layanan_kesehatan.id'), nullable=False)
    nama = Column(String, index=True)
    jenis_kamar = Column(String, index=True)
    informasi_pembayaran = Column(String, index=True)

    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())