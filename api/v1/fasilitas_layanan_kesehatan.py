from api.common_bucket import *
from database.database import get_db_reads, get_db_writes 
from crud import fasilitas_layanan_kesehatan as crud

from schemas import fasilitas_layanan_kesehatan as schemas


router = APIRouter()


@router.get("/api/v1/facility", response_model=BaseResponse[List[schemas.FasilitasLayananKesehatan]])
async def get_fasilitas_layanan_kesehatan(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    '''
    Get All Facility API Endpoint

    Endpoint ini memungkinkan untuk mendapatkan semua data fasilitas layanan kesehatan yang ada pada database.
    Endpoint ini dapat menerima parameter berupa skip dan limit.
    - Skip digunakan untuk menentukan data yang akan dilewati.
    - Limit digunakan untuk menentukan jumlah data yang akan ditampilkan.

    Response Body Example:
    Hasil akan dikembalikan dalam bentuk JSON. Hasil yang ditampilkan adalah semua data fasilitas layanan kesehatan yang ada pada database.
    '''
    facilities = crud.get_fasilitas_layanan_kesehatan_all(db, skip=skip, limit=limit)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fasilitas layanan kesehatan",
        data=facilities
        )

    if facilities is None:
        response.status = "404 Not Found"
        response.message = "Data fasilitas layanan kesehatan tidak ditemukan"
    return response

@router.get("/api/v1/facility/{facility_id}", response_model=BaseResponse[schemas.FasilitasLayananKesehatan])
async def get_fasilitas_layanan_kesehatan(
    facility_id: str, 
    db: Session = Depends(get_db_reads)
    ):
    '''
    Get Facility By ID API Endpoint

    Endpoint ini memungkinkan untuk mendapatkan data fasilitas layanan kesehatan berdasarkan ID yang diberikan.

    Response Body Example:
    Hasil akan dikembalikan dalam bentuk JSON. Hasil yang ditampilkan adalah data fasilitas layanan kesehatan yang memiliki ID sesuai.
    '''
    facility = crud.get_fasilitas_layanan_kesehatan(db, facility_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengambil data fasilitas layanan kesehatan",
        data=facility
        )
    
    return response

@router.post("/api/v1/facility", response_model=BaseResponse[schemas.FasilitasLayananKesehatan])
async def create_fasilitas_layanan_kesehatan(
    facility: schemas.FasilitasLayananKesehatanCreate, 
    db: Session = Depends(get_db_writes)
    ):
    '''
    Create New Facility API Endpoint

    Endpoint ini memungkinkan untuk menambahkan data fasilitas layanan kesehatan baru ke dalam database.

    Request Body Example:
    {
        "nama": "string",
        "alamat": "string",
        "tipe": "string"
    }

    Response Body Example:
    Hasil akan dikembalikan dalam bentuk JSON. Hasil yang ditampilkan adalah data fasilitas layanan kesehatan yang baru saja disimpan ke database.
    '''
    db_facility = crud.get_fasilitas_layanan_kesehatan_by_name(db, facility.nama)

    facility = crud.create_fasilitas_layanan_kesehatan(db, facility)

    response = BaseResponse(
        status="201 Created",
        message="Berhasil menambahkan fasilitas layanan kesehatan",
        data=facility
    )

    if db_facility:
        response = BaseResponse(
            status="400 Bad Request",
            message="Fasilitas layanan kesehatan sudah ada",
            data=facility
        )
    return response


@router.put("/api/v1/facility/{facility_id}", response_model=BaseResponse[schemas.FasilitasLayananKesehatan])
async def update_fasilitas_layanan_kesehatan(
    facility_id: str,
    facility: schemas.FasilitasLayananKesehatan,
    db: Session = Depends(get_db_writes)
    ):
    '''
    Update Facility By ID API Endpoint

    Endpoint ini memungkinkan untuk memperbarui data fasilitas layanan kesehatan berdasarkan ID yang diberikan.

    Request Body Example:
    {
        "nama": "string",
        "alamat": "string",
        "tipe": "string"
    }

    Response Body Example:
    Hasil akan dikembalikan dalam bentuk JSON. Hasil yang ditampilkan adalah data fasilitas layanan kesehatan yang baru saja diperbarui.
    '''
    db_facility = crud.get_fasilitas_layanan_kesehatan(db, facility_id)

    if db_facility is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data fasilitas layanan kesehatan tidak ditemukan",
            data=facility
        )

    facility.id = facility_id
    facility = crud.update_fasilitas_layanan_kesehatan(db, facility)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data fasilitas layanan kesehatan",
        data=facility
    )
    return response


@router.delete("/api/v1/facility/{facility_id}", response_model=BaseResponse[schemas.FasilitasLayananKesehatan])
async def delete_fasilitas_layanan_kesehatan(facility_id: str, db: Session = Depends(get_db_writes)):
    '''
    Delete Facility By ID API Endpoint

    Endpoint ini memungkinkan untuk menghapus data fasilitas layanan kesehatan berdasarkan ID yang diberikan.

    Response Body Example:
    Hasil akan dikembalikan dalam bentuk JSON. Hasil yang ditampilkan adalah data fasilitas layanan kesehatan yang baru saja dihapus dari database.
    '''
    db_facility = crud.get_fasilitas_layanan_kesehatan(db, facility_id)
    if db_facility is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data fasilitas layanan kesehatan tidak ditemukan",
            data=None
        )

    crud.delete_fasilitas_layanan_kesehatan(db, facility_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data fasilitas layanan kesehatan",
        data=db_facility
    )
    return response