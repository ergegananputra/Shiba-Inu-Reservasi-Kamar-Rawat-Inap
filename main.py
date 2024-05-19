from fastapi import Depends, FastAPI
from database.database import DBServerWrites

from api.v1.fasilitas_layanan_kesehatan import router as api_flk

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