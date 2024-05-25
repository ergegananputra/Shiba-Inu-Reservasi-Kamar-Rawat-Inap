from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import jenis_tempat_tidur as crud

from schemas import jenis_tempat_tidur as schemas

router = APIRouter()

@router.get("/api/v1/bedroom", response_model=list[schemas.JenisTempatTidur])
async def get_jenis_tempat_tidur(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    room_types = crud.get_jenis_tempat_tidur_all(db, skip=skip, limit=limit)
    if room_types is None:
        raise HTTPException(status_code=404, detail="Room type not found")
    return room_types

@router.get("/api/v1/bedroom/{room_type_id}", response_model=schemas.JenisTempatTidur)
async def get_jenis_tempat_tidur(
        room_type_id: str,
        db: Session = Depends(get_db_reads)
    ):
    room_type = crud.get_jenis_tempat_tidur(db, room_type_id)
    return room_type

@router.post("/api/v1/bedroom", response_model=schemas.JenisTempatTidur)
async def create_jenis_tempat_tidur(
        room_type: schemas.JenisTempatTidurCreate,
        db: Session = Depends(get_db_writes)
    ):
    db_room_type = crud.get_jenis_tempat_tidur_by_jenis_tempat_tidur(db, room_type.jenis_tempat_tidur)
    if db_room_type:
        raise HTTPException(status_code=400, detail="Room type already registered")
    return crud.create_jenis_tempat_tidur(db, room_type)

@router.put("/api/v1/bedroom/{room_type_id}", response_model=schemas.JenisTempatTidur)
async def update_jenis_tempat_tidur(
        room_type_id: str,
        room_type: schemas.JenisTempatTidur,
        db: Session = Depends(get_db_writes)
    ):
    db_room_type = crud.get_jenis_tempat_tidur(db, room_type_id)
    if db_room_type is None:
        raise HTTPException(status_code=404, detail="Room type not found")
    room_type.id = room_type_id
    return crud.update_jenis_tempat_tidur(db, room_type)

@router.delete("/api/v1/bedroom/{room_type_id}", response_model=schemas.JenisTempatTidur)
async def delete_jenis_tempat_tidur(room_type_id: str, db: Session = Depends(get_db_writes)):
    db_room_type = crud.get_jenis_tempat_tidur(db, room_type_id)
    if db_room_type is None:
        raise HTTPException(status_code=404, detail="Room type not found")
    return crud.delete_jenis_tempat_tidur(db, room_type_id)