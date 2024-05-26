from models.room_models import *
from sqlalchemy.sql.sqltypes import Double

class Kasur(DBServerWrites.Base):
    __tablename__ = "kasur"
    __table_args__ = {'extend_existing': True}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    fk_fkr = Column(UUIDType(binary=False), ForeignKey('fleet_kamar.id'), nullable=False)
    fk_sk = Column(UUIDType(binary=False), ForeignKey('status_kamar.id'), nullable=False)
    fk_jtt = Column(UUIDType(binary=False), ForeignKey('jenis_tempat_tidur.id'), nullable=False)
    fk_fdk = Column(UUIDType(binary=False), ForeignKey('fasilitas_detail_kamar.id'), nullable=False)

    tingkat_fasilitas_kesehatan = Column(String, index=True)
    biaya_pakai_per_hari = Column(Double, index=True)
    kode_kamar = Column(String, index=True)

    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())

