from models.room_models import *;

class FasilitasDetailKamar():
    __table_name__ = "fasilitas_detail_kamar"
    __table_args__ = {'extend_existing': True}

    id = Column(UUIDType(binary=False), primary_key= True, default=uuid.uuid4, unique=True, nullable=False)
    tabung_oksigen = Column(Integer, index=True)
    kamar_mandi = Column(Integer, index=True)
    infus = Column(Integer, index=True)
    nurse_call = Column(Integer, index=True)
    kasur_pendamping = Column(Integer, index=True)
    sofa = Column(Integer, index=True)
    lemari = Column(Integer, index=True)
    meja_makan_pasien = Column(Integer, index=True)
    meja_makan_pendamping = Column(Integer, index=True)
    televisi = Column(Integer, index=True)
    dispenser = Column(Integer, index=True)
    kulkas = Column(Integer, index=True)
    wastafel = Column(Integer, index=True)
    fk_fpr = Column(UUIDType(index=True), ForeignKey("pendingin_ruangan.id"))
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())

