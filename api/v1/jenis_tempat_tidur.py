from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import jenis_tempat_tidur as crud

from schemas import jenis_tempat_tidur as schemas

router = APIRouter()

@router.get("/api/v1/bedroom", response_model=BaseResponse[List[schemas.JenisTempatTidur]])
async def get_jenis_tempat_tidur(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    room_types = crud.get_jenis_tempat_tidur_all(db, skip=skip, limit=limit)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data jenis tempat tidur",
        data=room_types
    )

    if room_types is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data jenis tempat tidur tidak ditemukan",
            data=room_types
        )
    return response

@router.get("/api/v1/bedroom/{room_type_id}", response_model=BaseResponse[schemas.JenisTempatTidur])
async def get_jenis_tempat_tidur(
        room_type_id: str,
        db: Session = Depends(get_db_reads)
    ):
    room_type = crud.get_jenis_tempat_tidur(db, room_type_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data jenis tempat tidur",
        data=room_type
    )

    return response

@router.post("/api/v1/bedroom", response_model=BaseResponse[schemas.JenisTempatTidur])
async def create_jenis_tempat_tidur(
        room_type: schemas.JenisTempatTidurCreate,
        db: Session = Depends(get_db_writes)
    ):
    db_room_type = crud.get_jenis_tempat_tidur_by_jenis_tempat_tidur(db, room_type.jenis_tempat_tidur)

    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan jenis tempat tidur",
        data=room_type
    )

    if db_room_type:
        return BaseResponse(
            status="400 Bad Request",
            message="Jenis tempat tidur sudah ada",
            data=room_type
        )
    return response

@router.put("/api/v1/bedroom/{room_type_id}", response_model=BaseResponse[schemas.JenisTempatTidur])
async def update_jenis_tempat_tidur(
        room_type_id: str,
        room_type: schemas.JenisTempatTidur,
        db: Session = Depends(get_db_writes)
    ):
    db_room_type = crud.get_jenis_tempat_tidur(db, room_type_id)

    if db_room_type is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data jenis tempat tidur tidak ditemukan",
            data=room_type
        )
    
    room_type.id = room_type_id

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data jenis tempat tidur",
        data=room_type
    )

    return response

@router.delete("/api/v1/bedroom/{room_type_id}", response_model=BaseResponse[schemas.JenisTempatTidur])
async def delete_jenis_tempat_tidur(room_type_id: str, db: Session = Depends(get_db_writes)):
    db_room_type = crud.get_jenis_tempat_tidur(db, room_type_id)
    if db_room_type is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data jenis tempat tidur tidak ditemukan",
            data=None
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data jenis tempat tidur",
        data=db_room_type
    )

    return response