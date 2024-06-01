from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import status_kamar as crud

from schemas import status_kamar as schemas

router = APIRouter()


@router.get("/api/v1/room-status", response_model=BaseResponse[List[schemas.StatusKamar]])
async def get_status_kamar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_reads)):
    
    '''
    Get All Room Status API Endpoint

    Endpoint ini memungkinkan untuk mendapatkan semua data status kamar yang ada pada database.
    Endpoint ini dapat menerima parameter berupa skip dan limit.
    - skip digunakan untuk menentukan jumlah data yang akan dilewati.
    - limit digunakan untuk menentukan jumlah data yang akan ditampilkan.
    
    Response Body Example: Hasil akan dikembalikan dalam bentuk JSON. Hasil pencarian akan berada pada key "data".
   '''
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

    '''
    Get Room Status by ID API Endpoint

    Endpoint ini memungkinkan untuk mendapatkan data status kamar dari database berdasarkan ID yang diberikan.
    Endpoint ini dapat menerima parameter berupa ID status kamar.
    - room_status_id digunakan untuk mencari data status kamar yang mempunyai ID tertentu.
    
    Response Body Example: 
    Hasil dari akan dikembalikan dalam bentuk JSON. Jika data status kamar tidak ditemukan, respons akan berisi status "404 Not Found" dengan pesan yang sesuai. 
    Jika berhasil, respons akan berisi status "200 OK" bersama dengan data status kamar yang ditemukan.

   '''
        
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
    ):

    '''
    Create Status Kamar API Endpoint

    Endpoint ini memungkinkan untuk menambahkan data status kamar baru ke dalam database.
   
    Request Body Example: 
    {
        "status" : "String"
    }
    
    Response Body Example: 
    Hasil akan dikembalikan dalam bentuk JSON. Jika permintaan berhasil, respons akan berisi status "201 Created" bersama dengan data status kamar yang baru ditambahkan. 
    Jika status kamar sudah ada, respons akan berisi status "400 Bad Request" dengan pesan yang menjelaskan bahwa room status tersebut sudah ada.

    '''
    db_room = crud.get_status_kamar_bystatus(db, room.status)
    if db_room:
        return BaseResponse(
            status="400 Bad Request",
            message="Room status sudah ada",
            data=room
        )
    
    room = crud.create_status_kamar(db, room)

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

    '''
    Update Status Kamar API Endpoint

    Endpoint ini memungkinkan untuk memperbarui data status kamar yang sudah ada dalam database berdasarkan ID yang diberikan.
    Endpoint ini dapat menerima parameter berupa id.
    - room_status_id digunakan untuk mencari data status kamar yang mempunyai ID tertentu.

    Request Body Example: 
    {
        "status" : "String",
    }

    Response Body Example:
    Hasil dari permintaan akan dikembalikan dalam bentuk JSON. Jika data status kamar tidak ditemukan, respons akan berisi status "404 Not Found" dengan pesan yang sesuai. 
    Jika berhasil, respons akan berisi status "200 OK" bersama dengan data status kamar yang telah diperbarui.

    '''
    db_room_status = crud.get_status_kamar(db, room_status_id)
    if db_room_status is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data room status tidak ditemukan",
            data=room_status
        )
    room_status.id = room_status_id

    room_status = crud.update_status_kamar(db, room_status)


    response = BaseResponse(
        status="200 OK",
        message="Berhasil mengupdate data room status",
        data=room_status
    )

    return response


@router.delete("/api/v1/room-status/{room_status_id}", response_model=BaseResponse[schemas.StatusKamar])
async def delete_status_kamar(room_status_id: str, db: Session = Depends(get_db_writes)):

    '''
    Delete Status Kamar API Endpoint

    Endpoint ini memungkinkan untuk menghapus data status kamar dari database berdasarkan ID yang diberikan.
    Endpoint ini dapat menerima parameter berupa id.
    - room_status_id digunakan untuk mencari data status kamar yang mempunyai ID tertentui.

    Response Body Example:
    Hasil dari permintaan akan dikembalikan dalam bentuk JSON. Jika data status kamar tidak ditemukan, respons akan berisi status "404 Not Found" dengan pesan yang sesuai. 
    Jika berhasil, respons akan berisi status "200 OK" bersama dengan data status kamar yang dihapus.

    '''

    
    db_room_status = crud.get_status_kamar(db, room_status_id)
    if db_room_status is None:
        return BaseResponse(
            status="404 Not Found",
            message="Data room status tidak ditemukan",
            data=None
        )
    
    db_room_status = crud.delete_status_kamar(db, room_status_id)

    response = BaseResponse(
        status="200 OK",
        message="Berhasil menghapus data room status",
        data=db_room_status
    )

    return response   