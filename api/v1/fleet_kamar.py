from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import fleet_kamar as crud

from schemas import fleet_kamar as schemas

router = APIRouter()


@router.get("/api/v1/fleet", response_model=BaseResponse[List[schemas.FleetKamar]])
async def get_fleet_kamar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    fleet_kamar = crud.get_fleet_kamar_all(db, skip=skip, limit=limit)
    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fleet kamar",
        data=fleet_kamar
    )
    if fleet_kamar is None:
        response.status = "404 Not Found"
        response.message = "Data fleet kamar tidak ditemukan"
    return fleet_kamar

@router.get("/api/v1/fleet/{fleet_id}", response_model=BaseResponse[List[schemas.FleetKamar]])
async def get_fleet_kamar(
    fleet_kamar_id: str,
    db: Session = Depends(get_db_reads)
    ):
    fleet = crud.get_fleet_kamar(db, fleet_kamar_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fleet kamar",
        data=fleet
    )

    return response

@router.post("/api/v1/fleet/", response_model=BaseResponse[schemas.FleetKamar])
async def create_fleet_kamar(
    fleet_kamar: schemas.FleetKamarCreate,
    db: Session = Depends(get_db_writes)
    ) :

    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan fleet kamar",
        data=crud.create_fleet_kamar(db, fleet_kamar)
    )

    return response

@router.put("/api/v1/fleet/{fleet_id}", response_model=BaseResponse[List[schemas.FleetKamar]])
async def update_fleet_kamar(fleet_kamar_id: str, fleet_kamar: schemas.FleetKamar, db: Session = Depends(get_db_writes)):
    db_fleet_kamar = crud.get_fleet_kamar(db, fleet_kamar_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data fleet kamar",
        data=fleet_kamar
    )

    if db_fleet_kamar is None:
        response.status = "404 Not Found"
        response.message = "Data fleet kamar tidak ditemukan"
        return response
    
    fleet_kamar.id = fleet_kamar_id
    response.data = crud.update_fleet_kamar(db, fleet_kamar)

    return response

@router.delete("/api/v1/fleet/{fleet_id}", response_model=BaseResponse[List[schemas.FleetKamar]])
async def delete_fleet_kamar(fleet_kamar_id: str, db: Session = Depends(get_db_writes)):
    db_fleet_kamar = crud.get_fleet_kamar(db, fleet_kamar_id)
    if db_fleet_kamar is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data fleet kamar tidak ditemukan",
            data=None
        )
    
    crud.delete_fleet_kamar(db, fleet_kamar_id)
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data fleet kamar",
        data=db_fleet_kamar
    )

    return response

