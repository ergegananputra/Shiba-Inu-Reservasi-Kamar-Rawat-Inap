from sqlalchemy.orm import Session
from uuid import UUID
import models.pendingin_ruangan as models
import schemas.pendingin_ruangan as schemas

def get_pendingin_ruangan(db: Session, pendingin_ruangan_id: UUID):
    return db.query(models.PendinginRuangan) \
            .filter(models.PendinginRuangan.id == pendingin_ruangan_id) \
            .first()

def get_pendingin_ruangan_by_name(db: Session, nama: str):
    return db.query(models.PendinginRuangan) \
            .filter(models.PendinginRuangan.nama == nama) \
            .first()

def get_pendingin_ruangan_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PendinginRuangan) \
            .offset(skip) \
            .limit(limit) \
            .all()

def create_pendingin_ruangan(db: Session, pendingin_ruangan: schemas.PendinginRuanganCreate):
    db_pendingin_ruangan = models.PendinginRuangan(
        nama=pendingin_ruangan.nama
    )
    db.add(db_pendingin_ruangan)
    db.commit()
    db.refresh(db_pendingin_ruangan)
    return db_pendingin_ruangan

def update_pendingin_ruangan(db: Session, pendingin_ruangan: models.PendinginRuangan):
    db_pendingin_ruangan = db.query(models.PendinginRuangan) \
            .filter(models.PendinginRuangan.id == pendingin_ruangan.id) \
            .first()
    if not db_pendingin_ruangan:
        return None
    db_pendingin_ruangan.nama = pendingin_ruangan.nama
    db.commit()
    db.refresh(db_pendingin_ruangan)
    return db_pendingin_ruangan

def delete_pendingin_ruangan(db: Session, pendingin_ruangan_id: UUID):
    db_pendingin_ruangan = db.query(models.PendinginRuangan) \
            .filter(models.PendinginRuangan.id == pendingin_ruangan_id) \
            .first()
    if not db_pendingin_ruangan:
        return None
    db.delete(db_pendingin_ruangan)
    db.commit()
    return db_pendingin_ruangan
