from fastapi import Depends, FastAPI
from database.database import DBServerWrites

from api.v1.fasilitas_layanan_kesehatan import router as api_flk
from api.v1.fleet_kamar import router as api_fleet
from api.v1.jenis_tempat_tidur import router as api_jtt
from api.v1.status_kamar import router as api_sk
from api.v1.pendingin_ruangan import router as api_pr
from api.v1.kasur import router as api_kasur
from api.v1.main_advanced import router as api_main


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
# def get_db():
#     db = DBServerWrites.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@app.get("/")
async def read_root():
    return {"message": "Fast API is working"}


app.include_router(api_flk)
app.include_router(api_fleet)
app.include_router(api_jtt)
app.include_router(api_sk)
app.include_router(api_pr)
app.include_router(api_kasur)
app.include_router(api_main)

