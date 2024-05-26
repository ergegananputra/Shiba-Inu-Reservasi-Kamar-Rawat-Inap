from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import pendingin_ruangan as crud
from schemas import pendingin_ruangan as schemas

router = APIRouter()

@router.get("/api/v1/pendingin-ruang", response_model=BaseResponse[List[schemas.PendinginRuangan]])
async def get_pendingin_ruangan(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    pendingin = crud.get_pendingin_ruangan_all(db, skip=skip, limit=limit)
    if pendingin is None:
        return BaseResponse(
            status="404 Not Found",
            message="Pendingin Ruangan not found",
            data=pendingin
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data pendingin ruangan",
        data=pendingin
    )

    return response

@router.get("/api/v1/pendingin-ruang/{pendingin_ruangan_id}", response_model=BaseResponse[schemas.PendinginRuangan])
async def get_pendingin_ruangan_detail(pendingin_ruangan_id: str, db: Session = Depends(get_db_reads)):
    pendingin = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if pendingin is None:
        return BaseResponse(
            status="404 Not Found",
            message="Pendingin Ruangan not found",
            data=pendingin
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data pendingin ruangan",
        data=pendingin
    )

    return response

@router.post("/api/v1/pendingin-ruang", response_model=BaseResponse[schemas.PendinginRuangan])
async def create_pendingin_ruangan(pendingin_ruangan: schemas.PendinginRuanganCreate, db: Session = Depends(get_db_writes)):
    db_pendingin_ruangan = crud.get_pendingin_ruangan_by_name(db, pendingin_ruangan.nama)
    if db_pendingin_ruangan:
        return BaseResponse(
            status="400 Bad Request",
            message="Pendingin Ruangan name already exists",
            data=db_pendingin_ruangan
        )
    
    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan pendingin ruangan",
        data=crud.create_pendingin_ruangan(db, pendingin_ruangan)
    )

    return response

@router.put("/api/v1/pendingin-ruang/{pendingin_ruangan_id}", response_model=BaseResponse[schemas.PendinginRuangan])
async def update_pendingin_ruangan(
        pendingin_ruangan_id: str,
        pendingin: schemas.PendinginRuangan,
        db: Session = Depends(get_db_writes)
    ):
    db_pendingin_ruangan = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if db_pendingin_ruangan is None:
        return BaseResponse(
            status="404 Not Found",
            message="Pendingin Ruangan not found",
            data=pendingin
        )
    pendingin.id = pendingin_ruangan_id

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data pendingin ruangan",
        data=pendingin
    )

    return response

@router.delete("/api/v1/pendingin-ruang/{pendingin_ruangan_id}", response_model=BaseResponse[schemas.PendinginRuangan])
async def delete_pendingin_ruangan(pendingin_ruangan_id: str, db: Session = Depends(get_db_writes)):
    db_pendingin_ruangan = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if db_pendingin_ruangan is None:
        return BaseResponse(
            status="404 Not Found",
            message="Pendingin Ruangan not found",
            data=db_pendingin_ruangan
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data pendingin ruangan",
        data=db_pendingin_ruangan
    )

    return response