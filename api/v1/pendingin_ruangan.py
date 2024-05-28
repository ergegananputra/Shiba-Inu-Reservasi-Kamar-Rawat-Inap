from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import pendingin_ruangan as crud
from schemas import pendingin_ruangan as schemas

router = APIRouter()

@router.get("/api/v1/pendingin-ruang", response_model=BaseResponse[List[schemas.PendinginRuangan]])
async def get_pendingin_ruangan(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    '''

    Get All Pendingin Ruangan Endpoint

    Endpoint ini memungkinkan untuk mendapatkan semua data pendingin ruangan yang ada di database.
    Endpoint ini dapat menerima parameter berupa skip dan limit.
    - Skip digunakan untuk menentukan data yang akan dilewati.
    - Limit digunakan untuk menentukan jumlah data yang akan ditampilkan.

    Response Body Example:

    [
        {
            "id": str,
            "nama": str,
            "tipe": str,
            "lokasi": str
        }
    ]
    Hasil akan dikembalikan dalam bentuk JSON. Hasil pencarian akan berada pada key "data".
    '''
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
    '''
    Get Pendingin Ruangan Detail Endpoint

    Endpoint ini memungkinkan untuk mendapatkan detail data pendingin ruangan berdasarkan ID.

    Path Parameter:
    - pendingin_ruangan_id (str): ID dari pendingin ruangan yang ingin diambil detailnya.

    Response Body Example:

    {
        "id": str,
        "nama": str,
        "tipe": str,
        "lokasi": str
    }


    Hasil akan dikembalikan dalam bentuk JSON.
    '''
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
    '''
    Create Pendingin Ruangan Endpoint

    Endpoint ini memungkinkan untuk membuat data pendingin ruangan baru.

    Request Body Example:

    {
        "nama": str,
        "tipe": str,
        "lokasi": str
    }


    Response Body Example:

    {
        "id": str,
        "nama": str,
        "tipe": str,
        "lokasi": str
    }


    Hasil akan dikembalikan dalam bentuk JSON.
    '''
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
    '''
    Update Pendingin Ruangan Endpoint

    Endpoint ini memungkinkan untuk memperbarui data pendingin ruangan berdasarkan ID.

    Path Parameter:
    - pendingin_ruangan_id (str): ID dari pendingin ruangan yang ingin diperbarui.

    Request Body Example:

    {
        "nama": str,
        "tipe": str,
        "lokasi": str
    }


    Response Body Example:

    {
        "id": str,
        "nama": str,
        "tipe": str,
        "lokasi": str
    }


    Hasil akan dikembalikan dalam bentuk JSON.
    '''
    db_pendingin_ruangan = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if db_pendingin_ruangan is None:
        return BaseResponse(
            status="404 Not Found",
            message="Pendingin Ruangan not found",
            data=pendingin
        )
    pendingin.id = pendingin_ruangan_id

    pendingin = crud.update_pendingin_ruangan(db, pendingin)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data pendingin ruangan",
        data=pendingin
    )

    return response

@router.delete("/api/v1/pendingin-ruang/{pendingin_ruangan_id}", response_model=BaseResponse[schemas.PendinginRuangan])
async def delete_pendingin_ruangan(pendingin_ruangan_id: str, db: Session = Depends(get_db_writes)):
    '''
    Delete Pendingin Ruangan Endpoint

    Endpoint ini memungkinkan untuk menghapus data pendingin ruangan berdasarkan ID.

    Path Parameter:
    - pendingin_ruangan_id (str): ID dari pendingin ruangan yang ingin dihapus.

    Response Body Example:

    {
        "id": str,
        "nama": str,
        "tipe": str,
        "lokasi": str
    }


    Hasil akan dikembalikan dalam bentuk JSON.
    '''
    db_pendingin_ruangan = crud.get_pendingin_ruangan(db, pendingin_ruangan_id)
    if db_pendingin_ruangan is None:
        return BaseResponse(
            status="404 Not Found",
            message="Pendingin Ruangan not found",
            data=db_pendingin_ruangan
        )
    
    db_pendingin_ruangan = crud.delete_pendingin_ruangan(db, pendingin_ruangan_id)
    
    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data pendingin ruangan",
        data=db_pendingin_ruangan
    )

    return response