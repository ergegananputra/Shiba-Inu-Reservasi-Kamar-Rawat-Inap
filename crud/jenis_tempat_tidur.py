from sqlalchemy.orm import Session
from uuid import UUID
import models.jenis_tempat_tidur as models
import schemas.jenis_tempat_tidur as schemas

def get_jenis_tempat_tidur(db: Session, jenis_tempat_tidur_id: UUID):
    return db.query(models.JenisTempatTidur) \
            .filter(models.JenisTempatTidur.id == jenis_tempat_tidur_id) \
            .first()

def get_jenis_tempat_tidur_by_jenis_tempat_tidur(db: Session, jenis_tempat_tidur: str):
    return db.query(models.JenisTempatTidur) \
            .filter(models.JenisTempatTidur.jenis_tempat_tidur == jenis_tempat_tidur) \
            .first()

def get_jenis_tempat_tidur_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JenisTempatTidur) \
            .offset(skip) \
            .limit(limit) \
            .all()

def create_jenis_tempat_tidur(db: Session, jenis_tempat_tidur: schemas.JenisTempatTidurCreate):
    db_jenis_tempat_tidur = models.JenisTempatTidur(
        jenis_tempat_tidur=jenis_tempat_tidur.jenis_tempat_tidur,
        keterangan=jenis_tempat_tidur.keterangan
    )
    db.add(db_jenis_tempat_tidur)
    db.commit()
    db.refresh(db_jenis_tempat_tidur)
    return db_jenis_tempat_tidur

def update_jenis_tempat_tidur(db: Session, jenis_tempat_tidur: models.JenisTempatTidur):
    db_jenis_tempat_tidur = db.query(models.JenisTempatTidur) \
            .filter(models.JenisTempatTidur.id == jenis_tempat_tidur.id) \
            .first()
    db_jenis_tempat_tidur.jenis_tempat_tidur = jenis_tempat_tidur.jenis_tempat_tidur
    db_jenis_tempat_tidur.keterangan = jenis_tempat_tidur.keterangan
    db.commit()
    db.refresh(db_jenis_tempat_tidur)
    return db_jenis_tempat_tidur

def delete_jenis_tempat_tidur(db: Session, jenis_tempat_tidur_id: UUID):
    db_jenis_tempat_tidur = db.query(models.JenisTempatTidur) \
            .filter(models.JenisTempatTidur.id == jenis_tempat_tidur_id) \
            .first()
    db.delete(db_jenis_tempat_tidur)
    db.commit()
    return db_jenis_tempat_tidur