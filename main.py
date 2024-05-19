from typing import Union

from fastapi import Depends, FastAPI, HTTPException
from database.database import DBServerWrites

from sqlalchemy.orm import Session
from schemas import room_schemas as schemas
from crud import crud

import logging
app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    logging.error(f"An error occurred: {exc}")
    return {"message": "Internal Server Error"}, 500

try:
    DBServerWrites.Base.metadata.create_all(bind=DBServerWrites.engine)
except Exception as e:
    logging.error(f"An error occurred when creating the database tables: {e}")

#Dependency
def get_db():
    db = DBServerWrites.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/api/v1/facility", response_model=list[schemas.FasilitasLayananKesehatan])
async def get_fasilitas_layanan_kesehatan(skip: int = 0, limit: int = 100, db : Session= Depends(get_db)):
    facilities = crud.get_fasilitas_layanan_kesehatan_all(db, skip=skip, limit=limit)
    if facilities is None:
        raise HTTPException(status_code=404, detail="Facility not found")
    return facilities

@app.get("/api/v1/facility/{facility_id}", response_model=schemas.FasilitasLayananKesehatan)
async def get_fasilitas_layanan_kesehatan(
    facility_id: str, 
    db: Session = Depends(get_db)
    ):
    facility = crud.get_fasilitas_layanan_kesehatan(db, facility_id)
    return facility

@app.post("/api/v1/facility", response_model=schemas.FasilitasLayananKesehatan)
async def create_fasilitas_layanan_kesehatan(
    facility: schemas.FasilitasLayananKesehatanCreate, 
    db: Session = Depends(get_db)
    ) :
    db_facility = crud.get_fasilitas_layanan_kesehatan_by_name(db, facility.nama)
    if db_facility:
        raise HTTPException(status_code=400, detail="Facility already registered")
    return crud.create_fasilitas_layanan_kesehatan(db, facility)