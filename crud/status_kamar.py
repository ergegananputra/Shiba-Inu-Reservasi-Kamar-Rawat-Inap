from sqlalchemy.orm import Session
from uuid import UUID
import models.status_kamar as models
import schemas.status_kamar as schemas


def get_status_kamar(db: Session, status_kamar_id: UUID):
    return db.query(models.StatusKamar) \
            .filter(models.StatusKamar.id == status_kamar_id) \
            .first()

def get_status_kamar_bystatus(db: Session, status: str):
    return db.query(models.StatusKamar) \
            .filter(models.StatusKamar.status == status) \
            .first()

def get_status_kamar_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StatusKamar) \
            .offset(skip) \
            .limit(limit) \
            .all()

def create_status_kamar(db: Session, status_kamar: schemas.StatusKamarCreate):
    db_status_kamar = models.StatusKamar(
        status=status_kamar.status,
    )
    db.add(db_status_kamar)
    db.commit()
    db.refresh(db_status_kamar)
    return db_status_kamar

def update_status_kamar(db: Session, status_kamar: models.StatusKamar):
    db_status_kamar = db.query(models.StatusKamar) \
            .filter(models.StatusKamar.id == status_kamar.id) \
            .first()
    db_status_kamar.status = status_kamar.status
    db.commit()
    db.refresh(db_status_kamar)
    return db_status_kamar

def delete_status_kamar(db: Session, status_kamar_id: UUID):
    db_status_kamar = db.query(models.StatusKamar) \
            .filter(models.StatusKamar.id == status_kamar_id) \
            .first()
    db.delete(db_status_kamar)
    db.commit()
    return db_status_kamar
