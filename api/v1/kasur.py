from api.common_bucket import *
from database.database import get_db_reads, get_db_writes

from crud import kasur as crud
from schemas import kasur as schemas

router = APIRouter()

@router.get("/api/v1/bed", response_model=BaseResponse[List[schemas.Kasur]])
async def get_kasur(skip: int = 0, limit: int = 100, db: Session= Depends(get_db_reads)):
    beds = crud.get_kasur_all(db, skip=skip, limit=limit)
    if beds is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data kasur tidak ditemukan",
            data=beds
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data kasur",
        data=beds
    )

    return response

@router.get("/api/v1/bed/{bed_id}", response_model=BaseResponse[schemas.Kasur])
async def get_kasur(bed_id: str, db: Session= Depends(get_db_reads)):
    bed = crud.get_kasur(db, bed_id)
    if bed is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data kasur tidak ditemukan",
            data=bed
        )
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data kasur",
        data=bed
    )
    return response

@router.post("/api/v1/bed/{bed_id}", response_model=BaseResponse[schemas.Kasur])
async def create_kasur(bed: schemas.Kasur, db: Session = Depends(get_db_writes)):

    bed = crud.create_kasur(db, bed)

    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan kasur",
        data=bed
    )
    return response

@router.delete("/api/v1/bed/{bed_id}", response_model=BaseResponse[schemas.Kasur])
async def delete_kasur(bed_id: str, db: Session= Depends(get_db_writes)):
    db_kasur = crud.get_kasur(db, bed_id)
    if db_kasur:
        return BaseResponse(
            status="404 Not Found",
            message="Data kasur tidak ditemukan",
            data=db_kasur
        )
    
    db_kasur = crud.delete_kasur(db, bed_id)
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data kasur",
        data=db_kasur
    )

    return response

@router.put("/api/v1/bed/{bed_id}", response_model=BaseResponse[schemas.Kasur])
async def update_kasur(bed_id: str, bed: schemas.Kasur, db: Session = Depends(get_db_writes)):
    db_kasur = crud.get_kasur(db, bed_id)
    if db_kasur is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data kasur tidak ditemukan",
            data=bed
        )
    bed.id = bed_id

    bed = crud.update_kasur(db, bed)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data kasur",
        data=bed
    )
    return response
