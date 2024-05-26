from api.common_bucket import *
from database.database import get_db_reads, get_db_writes

from crud import kasur as crud
from schemas import kasur as schemas

router = APIRouter()

@router.get("/api/v1/bed", response_model=list[schemas.Kasur])
async def get_kasur(skip: int = 0, limit: int = 100, db: Session= Depends(get_db_reads)):
    beds = crud.get_kasur_all(db, skip=skip, limit=limit)
    if beds is None:
        raise HTTPException(status_code=404, detail="Beds not found")
    return beds

@router.get("/api/v1/bed/{bed_id}", response_model=list[schemas.Kasur])
async def get_kasur(bed_id: str, db: Session= Depends(get_db_reads)):
    bed = crud.get_kasur(db, bed_id)
    return bed
@router.post("/api/v1/bed/{bed_id}", response_model=schemas.Kasur)
async def create_kasur(bed: schemas.Kasur, db: Session = Depends(get_db_writes)):
    return crud.create_kasur(db, bed)
@router.delete("/api/v1/bed/{bed_id}", response_model=schemas.Kasur)
async def delete_kasur(bed_id: str, db: Session= Depends(get_db_writes)):
    db_kasur = crud.get_kasur(db, bed_id)
    if db_kasur:
        raise HTTPException(status_code=404, detail="Bed not found")
    return crud.delete_kasur(db, bed_id)

@router.put("/api/v1/bed/{bed_id}", response_model=schemas.Kasur)
async def update_kasur(bed_id: str, bed: schemas.Kasur, db: Session = Depends(get_db_writes)):
    db_kasur = crud.get_kasur(db, bed_id)
    if db_kasur is None:
        raise HTTPException(status_code=404, detail="Bed not found")
    bed.id = bed_id
    return crud.update_kasur(db, bed)
