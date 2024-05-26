from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import status_kamar as crud

from schemas import status_kamar as schemas

router = APIRouter()


@router.get("/api/v1/room-status", response_model=BaseResponse[List[schemas.StatusKamar]])
async def get_status_kamar(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    rooms = crud.get_status_kamar_all(db, skip=skip, limit=limit)
    if rooms is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data room status tidak ditemukan",
            data=rooms
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data room status",
        data=rooms
    )

    return response

@router.get("/api/v1/room-status/{room_status_id}", response_model=BaseResponse[schemas.StatusKamar])
async def get_status_kamar(
    room_status_id: str,
    db: Session = Depends(get_db_reads)
    ):
    room = crud.get_status_kamar(db, room_status_id)
    if room is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data room status tidak ditemukan",
            data=room
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data room status",
        data=room
    )

    return response

@router.post("/api/v1/room-status", response_model=BaseResponse[schemas.StatusKamar])
async def create_status_kamar(
    room: schemas.StatusKamarCreate,
    db: Session = Depends(get_db_writes)
    ) :
    db_room = crud.get_status_kamar_bystatus(db, room.status)
    if db_room:
        return BaseResponse(
            status="400 Bad Request",
            message="Room status sudah ada",
            data=room
        )
    
    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan room status",
        data=room
    )

    return response

@router.put("/api/v1/room-status/{room_status_id}", response_model=BaseResponse[schemas.StatusKamar])
async def update_status_kamar(
        room_status_id: str,
        room_status: schemas.StatusKamar,
        db: Session = Depends(get_db_writes)
    ):
    db_room_status = crud.get_status_kamar(db, room_status_id)
    if db_room_status is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data room status tidak ditemukan",
            data=room_status
        )
    room_status.id = room_status_id

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data room status",
        data=room_status
    )

    return response

@router.delete("/api/v1/room-status/{room_status_id}", response_model=BaseResponse[schemas.StatusKamar])
async def delete_status_kamar(room_status_id: str, db: Session = Depends(get_db_writes)):
    db_room_status = crud.get_status_kamar(db, room_status_id)
    if db_room_status is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data room status tidak ditemukan",
            data=None
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data room status",
        data=db_room_status
    )

    return response 