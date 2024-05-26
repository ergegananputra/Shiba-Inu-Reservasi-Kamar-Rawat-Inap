from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import pendingin_ruangan as crud
from schemas import pendingin_ruangan as schemas

router = APIRouter()

@router.get("/api/v1/pendingin-ruang", response_model=list[schemas.PendinginRuangan])
async def get_pendingin_ruangan(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    pendingin = crud.get_pendingin_ruangan_all(db, skip=skip, limit=limit)
    if pendingin is None:
        raise HTTPException(status_code=404, detail="Pendingin Ruangan not found")
    return pendingin

@router.get("/api/v1/pendingin-ruang/{pendingin_ruangan_id}", response_model=schemas.PendinginRuangan)
async def get_pendingin_ruangan_detail(pendingin_ruangan_id: str, db: Session = Depends(get_db_reads)):
    pendingin = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if pendingin is None:
        raise HTTPException(status_code=404, detail="Pendingin Ruangan not found")
    return pendingin

@router.post("/api/v1/pendingin-ruang", response_model=schemas.PendinginRuangan)
async def create_pendingin_ruangan(pendingin_ruangan: schemas.PendinginRuanganCreate, db: Session = Depends(get_db_writes)):
    db_pendingin_ruangan = crud.get_pendingin_ruangan_by_name(db, pendingin_ruangan.nama)
    if db_pendingin_ruangan:
        raise HTTPException(status_code=400, detail="Pendingin Ruangan already registered")
    return crud.create_pendingin_ruangan(db, pendingin_ruangan)

@router.put("/api/v1/pendingin-ruang/{pendingin_ruangan_id}", response_model=schemas.PendinginRuangan)
async def update_pendingin_ruangan(
        pendingin_ruangan_id: str,
        pendingin: schemas.PendinginRuangan,
        db: Session = Depends(get_db_writes)
    ):
    db_pendingin_ruangan = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if db_pendingin_ruangan is None:
        raise HTTPException(status_code=404, detail="Pendingin Ruangan name not found")
    pendingin.id = pendingin_ruangan_id
    return crud.update_pendingin_ruangan(db, pendingin)

@router.delete("/api/v1/pendingin-ruang/{pendingin_ruangan_id}", response_model=schemas.PendinginRuangan)
async def delete_pendingin_ruangan(pendingin_ruangan_id: str, db: Session = Depends(get_db_writes)):
    db_pendingin_ruangan = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if db_pendingin_ruangan is None:
        raise HTTPException(status_code=404, detail="Pendingin Ruangan name not found")
    return crud.delete_pendingin_ruangan(db, pendingin_ruangan_id)