from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import pendingin_ruangan as pr_crud
from crud import fasilitas_detail_kamar as crud

from schemas import fasilitas_detail_kamar as schemas

router = APIRouter()


@router.get("/api/v1/room-details", response_model=BaseResponse[List[schemas.FasilitasDetailKamar]])
async def get_fasilitas_detail_kamar(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    details = crud.get_fasilitas_detail_kamar(db, skip=skip, limit=limit)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fasilitas detail kamar",
        data=details
        )

    if details is None:
        response.status = "404 Not Found"
        response.message = "Data fasilitas detail kamar tidak ditemukan"
    return response

@router.get("/api/v1/room-details/{details_id}", response_model=BaseResponse[schemas.FasilitasDetailKamar])
async def get_fasilitas_detail_kamar(
    details_id: str,
    db: Session = Depends(get_db_reads)
    ):
    details = crud.get_fasilitas_detail_kamar_by_id(db, details_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fasilitas detail kamar",
        data=details
        )

    return response

@router.post("/api/v1/room-details", response_model=BaseResponse[schemas.FasilitasDetailKamar])
async def create_fasilitas_detail_kamar(
    details: schemas.FasilitasDetailKamar,
    db: Session = Depends(get_db_writes)
    ) :

    fpr = pr_crud.get_pendingin_ruangan(db, details.fk_fpr) if details.fk_fpr is not None else None
    if fpr is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data fasilitas pendukung ruangan tidak ditemukan",
            data=None
        )

    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan fasilitas detail kamar",
        data=crud.create_fasilitas_detail_kamar(db, details)
        )

    return response

@router.put("/api/v1/room-details/{details_id}", response_model=BaseResponse[schemas.FasilitasDetailKamar])
async def update_fasilitas_detail_kamar(
        details_id: str,
        details_type: schemas.FasilitasDetailKamar,
        db: Session = Depends(get_db_writes)
    ):
    db_details = crud.get_fasilitas_detail_kamar_by_id(db, details_id)

    if db_details is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data fasilitas detail kamar tidak ditemukan",
            data=None
        )
    
    details_type.id = details_id

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengubah data fasilitas detail kamar",
        data=crud.update_fasilitas_detail_kamar(db, details_type)
        )

    return response

@router.delete("/api/v1/room-details/{details_id}", response_model=BaseResponse[schemas.FasilitasDetailKamar])
async def delete_fasilitas_detail_kamar(details_id: str, db: Session = Depends(get_db_writes)):
    db_details = crud.get_fasilitas_detail_kamar_by_id(db, details_id)

    if db_details is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data fasilitas detail kamar tidak ditemukan",
            data=None
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data fasilitas detail kamar",
        data=crud.delete_fasilitas_detail_kamar(db, details_id)
        )
    return response