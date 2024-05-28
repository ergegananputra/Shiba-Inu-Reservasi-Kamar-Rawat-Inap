from sqlalchemy.orm import Session
from uuid import UUID
import models.fleet_kamar as models
import schemas.fleet_kamar as schemas


def get_fleet_kamar(db: Session, fleet_kamar_id: UUID):
    return db.query(models.FleetKamar) \
        .filter(models.FleetKamar.id == fleet_kamar_id) \
        .first()


def get_fleet_kamar_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FleetKamar) \
        .offset(skip) \
        .limit(limit) \
        .all()


def create_fleet_kamar(db: Session, fleet_kamar: schemas.FleetKamarCreate):
    db_fleet_kamar = models.FleetKamar(
        fk_flk=fleet_kamar.fk_flk,
        nama=fleet_kamar.nama,
        jenis_kamar=fleet_kamar.jenis_kamar,
        informasi_pembayaran=fleet_kamar.informasi_pembayaran
    )
    db.add(db_fleet_kamar)
    db.commit()
    db.refresh(db_fleet_kamar)
    return db_fleet_kamar


def update_fleet_kamar(db: Session, fleet_kamar: models.FleetKamar):
    db_fleet_kamar = db.query(models.FleetKamar) \
        .filter(models.FleetKamar.id == fleet_kamar.id) \
        .first()
    db_fleet_kamar.fk_flk = fleet_kamar.fk_flk
    db_fleet_kamar.nama = fleet_kamar.nama
    db_fleet_kamar.jenis_kamar = fleet_kamar.jenis_kamar
    db_fleet_kamar.informasi_pembayaran = fleet_kamar.informasi_pembayaran
    db.commit()
    db.refresh(db_fleet_kamar)
    return db_fleet_kamar


def delete_fleet_kamar(db: Session, fleet_kamar_id: UUID):
    db_fleet_kamar = db.query(models.FleetKamar) \
        .filter(models.FleetKamar.id == fleet_kamar_id) \
        .first()
    db.delete(db_fleet_kamar)
    db.commit()
    return db_fleet_kamar
