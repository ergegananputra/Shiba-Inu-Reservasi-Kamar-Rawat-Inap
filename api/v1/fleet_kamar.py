from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import fleet_kamar as crud

from schemas import fleet_kamar as schemas

router = APIRouter()


@router.get("/api/v1/fleet", response_model=list[schemas.FleetKamar])
async def get_fleet_kamar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    fleet_kamar = crud.get_fleet_kamar_all(db, skip=skip, limit=limit)
    if fleet_kamar is None:
        raise HTTPException(status_code=404, detail="Fleet not found")
    return fleet_kamar

@router.get("/api/v1/fleet/{fleet_id}", response_model=list[schemas.FleetKamar])
async def get_fleet_kamar(
    fleet_kamar_id: str,
    db: Session = Depends(get_db_reads)
    ):
    fleet = crud.get_fleet_kamar(db, fleet_kamar_id)
    return fleet

@router.post("/api/v1/fleet/", response_model=schemas.FleetKamar)
async def create_fleet_kamar(
    fleet_kamar: schemas.FleetKamarCreate,
    db: Session = Depends(get_db_writes)
    ) :
    return crud.create_fleet_kamar(db, fleet_kamar)

@router.put("/api/v1/fleet/{fleet_id}", response_model=list[schemas.FleetKamar])
async def update_fleet_kamar(fleet_kamar_id: str, fleet_kamar: schemas.FleetKamar, db: Session = Depends(get_db_writes)):
    db_fleet_kamar = crud.get_fleet_kamar(db, fleet_kamar_id)
    if db_fleet_kamar is None:
        raise HTTPException(status_code=404, detail="Fleet not found")
    fleet_kamar.id = fleet_kamar_id
    return crud.update_fleet_kamar(db, fleet_kamar)

@router.delete("/api/v1/fleet/{fleet_id}", response_model=list[schemas.FleetKamar])
async def delete_fleet_kamar(fleet_kamar_id: str, db: Session = Depends(get_db_writes)):
    db_fleet_kamar = crud.get_fleet_kamar(db, fleet_kamar_id)
    if db_fleet_kamar is None:
        raise HTTPException(status_code=404, detail="Fleet Kamar not found")
    return crud.delete_fleet_kamar(db, fleet_kamar_id)

