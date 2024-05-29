from api.common_bucket import *
from database.database import get_db_reads, get_db_writes 
from crud import fasilitas_layanan_kesehatan as crud

from schemas import fasilitas_layanan_kesehatan as schemas


router = APIRouter()


@router.get("/api/v1/facility", response_model=BaseResponse[List[schemas.FasilitasLayananKesehatan]])
async def get_fasilitas_layanan_kesehatan(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    facilities = crud.get_fasilitas_layanan_kesehatan_all(db, skip=skip, limit=limit)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fasilitas layanan kesehatan",
        data=facilities
        )

    if facilities is None:
        response.status = "404 Not Found"
        response.message = "Data fasilitas layanan kesehatan tidak ditemukan"
    return response

@router.get("/api/v1/facility/{facility_id}", response_model=BaseResponse[List[schemas.FasilitasLayananKesehatan]])
async def get_fasilitas_layanan_kesehatan(
    facility_id: str, 
    db: Session = Depends(get_db_reads)
    ):
    facility = crud.get_fasilitas_layanan_kesehatan(db, facility_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fasilitas layanan kesehatan",
        data=facility
        )
    
    return response

@router.post("/api/v1/facility", response_model=BaseResponse[schemas.FasilitasLayananKesehatan])
async def create_fasilitas_layanan_kesehatan(
    facility: schemas.FasilitasLayananKesehatanCreate, 
    db: Session = Depends(get_db_writes)
    ) :
    db_facility = crud.get_fasilitas_layanan_kesehatan_by_name(db, facility.nama)
    if db_facility:
        response = BaseResponse(
            status="400 Bad Request",
            message="Fasilitas layanan kesehatan sudah ada"
        )
    
    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan fasilitas layanan kesehatan",
        data=crud.create_fasilitas_layanan_kesehatan(db, facility)
        )

    return response