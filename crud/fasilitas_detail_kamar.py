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
        nama=fasilitas_detail_kamar.nama,
        alamat=fasilitas_detail_kamar.alamat
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