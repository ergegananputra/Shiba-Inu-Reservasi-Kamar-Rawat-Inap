from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import fasilitas_detail_kamar as crud

from schemas import fasilitas_detail_kamar as schemas

router = APIRouter()


@router.get("/api/v1/room-details", response_model=list[schemas.FasilitasDetailKamar])
async def get_fasilitas_detail_kamar(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    details = crud.get_fasilitas_detail_kamar(db, skip=skip, limit=limit)
    if details is None:
        raise HTTPException(status_code=404, detail="details not found")
    return details

@router.get("/api/v1/room-details/{details_id}", response_model=schemas.FasilitasDetailKamar)
async def get_fasilitas_detail_kamar(
    details_id: str,
    db: Session = Depends(get_db_reads)
    ):
    details = crud.get_fasilitas_detail_kamar(db, details_id)
    return details

@router.post("/api/v1/room-details", response_model=schemas.FasilitasDetailKamar)
async def create_fasilitas_detail_kamar(
    details: schemas.FasilitasDetailKamar,
    db: Session = Depends(get_db_writes)
    ) :
    db_details = crud.get_fasilitas_detail_kamar(db, details.nama)
    if db_details:
        raise HTTPException(status_code=400, detail="Details already registered")
    return crud.create_fasilitas_detail_kamar(db, details)

@router.put("/api/v1/room-details/{details_id}", response_model=schemas.FasilitasDetailKamar)
async def update_fasilitas_detail_kamar(
        details_id: str,
        details_type: schemas.FasilitasDetailKamar,
        db: Session = Depends(get_db_writes)
    ):
    db_details = crud.get_fasilitas_detail_kamar(db, details_id)
    if db_details is None:
        raise HTTPException(status_code=404, detail="Details type not found")
    details_type.id = details_id
    return crud.update_fasilitas_detail_kamar(db, details_type)

@router.delete("/api/v1/room-details/{details_id}", response_model=schemas.FasilitasDetailKamar)
async def delete_fasilitas_detail_kamar(details_id: str, db: Session = Depends(get_db_writes)):
    db_details = crud.get_fasilitas_detail_kamar(db, details_id)
    if db_details is None:
        raise HTTPException(status_code=404, detail="Details type not found")
    return crud.delete_fasilitas_detail_kamar(db, details_id)