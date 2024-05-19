from api.common_bucket import *
from database.database import get_db_reads, get_db_writes 
from crud import fasilitas_layanan_kesehatan as crud

from schemas import fasilitas_layanan_kesehatan as schemas

router = APIRouter()


@router.get("/api/v1/facility", response_model=list[schemas.FasilitasLayananKesehatan])
async def get_fasilitas_layanan_kesehatan(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    facilities = crud.get_fasilitas_layanan_kesehatan_all(db, skip=skip, limit=limit)
    if facilities is None:
        raise HTTPException(status_code=404, detail="Facility not found")
    return facilities

@router.get("/api/v1/facility/{facility_id}", response_model=schemas.FasilitasLayananKesehatan)
async def get_fasilitas_layanan_kesehatan(
    facility_id: str, 
    db: Session = Depends(get_db_reads)
    ):
    facility = crud.get_fasilitas_layanan_kesehatan(db, facility_id)
    return facility

@router.post("/api/v1/facility", response_model=schemas.FasilitasLayananKesehatan)
async def create_fasilitas_layanan_kesehatan(
    facility: schemas.FasilitasLayananKesehatanCreate, 
    db: Session = Depends(get_db_writes)
    ) :
    db_facility = crud.get_fasilitas_layanan_kesehatan_by_name(db, facility.nama)
    if db_facility:
        raise HTTPException(status_code=400, detail="Facility already registered")
    return crud.create_fasilitas_layanan_kesehatan(db, facility)