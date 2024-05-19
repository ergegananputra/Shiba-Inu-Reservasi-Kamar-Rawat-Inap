from sqlalchemy.orm import Session

from models.room_models import *
from schemas.room_schemas import *
from uuid import UUID

def get_fasilitas_layanan_kesehatan(db: Session, fasilitas_layanan_kesehatan_id: UUID):
    return db.query(FailitasLayananKesehatan) \
            .filter(FailitasLayananKesehatan.id == fasilitas_layanan_kesehatan_id) \
            .first()

def get_fasilitas_layanan_kesehatan_by_name(db: Session, nama: str):
    return db.query(FailitasLayananKesehatan) \
            .filter(FailitasLayananKesehatan.nama == nama) \
            .first()

def get_fasilitas_layanan_kesehatan_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FailitasLayananKesehatan) \
            .offset(skip) \
            .limit(limit) \
            .all()

def create_fasilitas_layanan_kesehatan(db: Session, fasilitas_layanan_kesehatan: FasilitasLayananKesehatanCreate):
    db_fasilitas_layanan_kesehatan = FailitasLayananKesehatan(
        id=fasilitas_layanan_kesehatan.id,
        nama=fasilitas_layanan_kesehatan.nama,
        alamat=fasilitas_layanan_kesehatan.alamat
    )
    db.add(db_fasilitas_layanan_kesehatan)
    db.commit()
    db.refresh(db_fasilitas_layanan_kesehatan)
    return db_fasilitas_layanan_kesehatan

def update_fasilitas_layanan_kesehatan(db: Session, fasilitas_layanan_kesehatan: FasilitasLayananKesehatan):
    db_fasilitas_layanan_kesehatan = db.query(FailitasLayananKesehatan) \
            .filter(FailitasLayananKesehatan.id == fasilitas_layanan_kesehatan.id) \
            .first()
    db_fasilitas_layanan_kesehatan.nama = fasilitas_layanan_kesehatan.nama
    db_fasilitas_layanan_kesehatan.alamat = fasilitas_layanan_kesehatan.alamat
    db.commit()
    db.refresh(db_fasilitas_layanan_kesehatan)
    return db_fasilitas_layanan_kesehatan

def delete_fasilitas_layanan_kesehatan(db: Session, fasilitas_layanan_kesehatan_id: UUID):
    db_fasilitas_layanan_kesehatan = db.query(FailitasLayananKesehatan) \
            .filter(FailitasLayananKesehatan.id == fasilitas_layanan_kesehatan_id) \
            .first()
    db.delete(db_fasilitas_layanan_kesehatan)
    db.commit()
    return db_fasilitas_layanan_kesehatan



