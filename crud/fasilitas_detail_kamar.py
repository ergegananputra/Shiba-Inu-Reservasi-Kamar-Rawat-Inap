from sqlalchemy.orm import Session
from uuid import UUID
import models.fasilitas_detail_kamar as models
import schemas.fasilitas_detail_kamar as schemas


def get_fasilitas_detail_kamar(db: Session, fasilitas_detail_kamar_id: UUID):
    return db.query(models.det) \
            .filter(models.FasilitasDetailKamar.id == fasilitas_detail_kamar_id) \
            .first()

def get_fasilitas_detail_kamar(db: Session, nama: str):
    return db.query(models.FasilitasDetailKamar) \
            .filter(models.FasilitasDetailKamar.nama == nama) \
            .first()

def get_fasilitas_detail_kamar(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FasilitasDetailKamar) \
            .offset(skip) \
            .limit(limit) \
            .all()

def create_fasilitas_detail_kamar(db: Session, fasilitas_detail_kamar: schemas.FasilitasDetailKamar):
    db_fasilitas_detail_kamar = models.FasilitasDetailKamar(
        fk_fpr=fasilitas_detail_kamar.fk_fpr,
        kamar_mandi=fasilitas_detail_kamar.kamar_mandi,
        tabung_oksigen = fasilitas_detail_kamar.tabung_oksigen,
        infus = fasilitas_detail_kamar.infus,
        nurse_call = fasilitas_detail_kamar.nurse_call,
        kasur_pendamping = fasilitas_detail_kamar.kasur_pendamping,
        sofa = fasilitas_detail_kamar.sofa,
        lemari = fasilitas_detail_kamar.lemari,
        meja_makan_pasien = fasilitas_detail_kamar.meja_makan_pasien,
        meja_makan_pendamping = fasilitas_detail_kamar.meja_makan_pendamping,
        televisi = fasilitas_detail_kamar.televisi,
        dispenser = fasilitas_detail_kamar.dispenser,
        kulkas = fasilitas_detail_kamar.kulkas,
        wastafel = fasilitas_detail_kamar.wastafel
        )
    db.add(db_fasilitas_detail_kamar)
    db.commit()
    db.refresh(db_fasilitas_detail_kamar)
    return db_fasilitas_detail_kamar

def update_fasilitas_detail_kamar(db: Session, fasilitas_detail_kamar: models.FasilitasDetailKamar):
    db_fasilitas_detail_kamar = db.query(models.FasilitasDetailKamar) \
            .filter(models.FasilitasDetailKamar.id == fasilitas_detail_kamar.id) \
            .first()
    db_fasilitas_detail_kamar.nama = fasilitas_detail_kamar.nama
    db_fasilitas_detail_kamar.alamat = fasilitas_detail_kamar.alamat
    db.commit()
    db.refresh(db_fasilitas_detail_kamar)
    return db_fasilitas_detail_kamar

def delete_fasilitas_detail_kamar(db: Session, fasilitas_detail_kamar: UUID):
    db_fasilitas_detail_kamar = db.query(models.FasilitasDetailKamar) \
            .filter(models.FasilitasDetailKamar.id == fasilitas_detail_kamar) \
            .first()
    db.delete(db_fasilitas_detail_kamar)
    db.commit()
    return db_fasilitas_detail_kamar