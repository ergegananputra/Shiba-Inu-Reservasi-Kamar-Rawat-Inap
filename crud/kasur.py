from sqlalchemy.orm import Session
from uuid import UUID
import models.kasur as models
import schemas.kasur as schemas


def get_kasur(db: Session, kasur_id: UUID):
    return db.query(models.Kasur)\
        .filter(models.Kasur.id == kasur_id)\
        .first()


def get_kasur_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Kasur) \
        .offset(skip) \
        .limit(limit) \
        .all()


def create_kasur(db: Session, kasur: schemas.KasurCreate):
    db_kasur = models.Kasur(
        fk_fkr=kasur.fk_fkr,
        fk_sk=kasur.fk_sk,
        fk_jtt=kasur.fk_jtt,
        fk_fdk=kasur.fk_fdk,
        tingkat_fasilitas_kesehatan=kasur.tingkat_fasilitas_kesehatan,
        biaya_pakai_per_hari=kasur.biaya_pakai_per_hari,
        kode_kamar=kasur.kode_kamar
    )
    db.add(db_kasur)
    db.commit()
    db.refresh(db_kasur)
    return db_kasur


def update_kasur(db: Session, kasur: models.Kasur):
    db_kasur = db.query(models.Kasur) \
        .filter(models.Kasur.id == kasur.id) \
        .first()

    db_kasur.fk_fkr = kasur.fk_fkr
    db_kasur.fk_sk = kasur.fk_sk
    db_kasur.fk_jtt = kasur.fk_jtt
    db_kasur.fk_fdk = kasur.fk_fdk
    db_kasur.tingkat_fasilitas_kesehatan = kasur.tingkat_fasilitas_kesehatan
    db_kasur.biaya_pakai_per_hari = kasur.biaya_pakai_per_hari
    db_kasur.kode_kamar = kasur.kode_kamar

    db.commit()
    db.refresh(db_kasur)
    return db_kasur


def delete_kasur(db: Session, kasur_id: UUID):
    db_kasur = db.query(models.Kasur) \
        .filter(models.Kasur.id == kasur_id) \
        .first()
    db.delete(db_kasur)
    db.commit()
    return db_kasur
