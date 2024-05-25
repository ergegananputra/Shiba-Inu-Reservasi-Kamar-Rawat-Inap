from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import status_kamar as crud

from schemas import status_kamar as schemas

router = APIRouter()


@router.get("/api/v1/room-status", response_model=list[schemas.StatusKamar])
async def get_status_kamar(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    rooms = crud.get_status_kamar_all(db, skip=skip, limit=limit)
    if rooms is None:
        raise HTTPException(status_code=404, detail="Room status not found")
    return rooms

@router.get("/api/v1/room-status/{room_status_id}", response_model=schemas.StatusKamar)
async def get_status_kamar(
    room_status_id: str,
    db: Session = Depends(get_db_reads)
    ):
    room = crud.get_status_kamar(db, room_status_id)
    return room

@router.post("/api/v1/room-status", response_model=schemas.StatusKamar)
async def create_status_kamar(
    room: schemas.StatusKamarCreate,
    db: Session = Depends(get_db_writes)
    ) :
    db_room = crud.get_status_kamar_bystatus(db, room.status)
    if db_room:
        raise HTTPException(status_code=400, detail="Room status already registered")
    return crud.create_status_kamar(db, room)

@router.put("/api/v1/room-status/{room_status_id}", response_model=schemas.StatusKamar)
async def update_status_kamar(
        room_status_id: str,
        room_status: schemas.StatusKamar,
        db: Session = Depends(get_db_writes)
    ):
    db_room_status = crud.get_status_kamar(db, room_status_id)
    if db_room_status is None:
        raise HTTPException(status_code=404, detail="Room status not found")
    room_status.id = room_status_id
    return crud.update_status_kamar(db, room_status)

@router.delete("/api/v1/room-status/{room_status_id}", response_model=schemas.StatusKamar)
async def delete_status_kamar(room_status_id: str, db: Session = Depends(get_db_writes)):
    db_room_status = crud.get_status_kamar(db, room_status_id)
    if db_room_status is None:
        raise HTTPException(status_code=404, detail="Room status not found")
    return crud.delete_status_kamar(db, room_status_id)