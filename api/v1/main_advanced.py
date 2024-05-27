from api.common_bucket import *
from database.database import get_db_reads 
from crud import main_advanced as crud

from schemas import main_advanced as schemas

router = APIRouter()


@router.get("/api/v1/advanced", response_model=BaseResponse[List[dict]])
async def get_all_advanced(
    skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)
    ) -> BaseResponse[List[dict]]:
    '''
    Get All Advanced API Endpoint

    Endpoint ini memungkinkan untuk mendapatkan semua data yang ada pada database.
    Endpoint ini dapat menerima parameter berupa skip dan limit.
    - Skip digunakan untuk menentukan data yang akan dilewati.
    - Limit digunakan untuk menentukan jumlah data yang akan ditampilkan.

    Request Body Example:
    {
        "skip" : Int,
        "limit" : Int,
    }

    Response Body Example:
    Hasil akan dikembalikan dalam bentuk JSON. Hasil pencarian akan berada pada key "data".
    '''

    request: schemas.SearchAdvancedRequest = schemas.SearchAdvancedRequest(
        keyword="",
        fields="*",
        select="*",
        limit=limit,
        page=skip,
        sort="asc"
    )

    keyword : str = request.keyword.lower()
    fields : list[str] = ["*"] if request.fields == "*" else [item for item in "".join(request.fields.lower().split()).split(",") if "." in item]
    select : list[str] = ["*"] if request.select == "*" else [item for item in "".join(request.select.lower().split()).split(",") if "." in item]
    limit : int = request.limit if request.limit > 0 else 100
    page : int = request.page if request.page > 0 else 1
    sort : str = request.sort.lower() if request.sort.lower() in ["asc", "desc"] else "asc"

    result = await search(db, keyword, fields, select, limit, page, sort)


    response = BaseResponse(
        status="200 OK",
        message="Data found",
        data=result
    )

    if result is None:
        response.status = "404 Not Found"
        response.message = "Data not found"

    return response



@router.post("/api/v1/advanced/search", response_model=BaseResponse[List[dict]])
async def search_advanced(
        request: schemas.SearchAdvancedRequest,
        db : Session= Depends(get_db_reads)
        ) -> BaseResponse[List[dict]] : 
    '''
    Search Advanced API Endpoint

    Endpoint ini memungkinkan untuk melakukan pencarian data dengan lebih spesifik.
    Endpoin ini dapat menerima parameter berupa keyword, fields, select, limit, page, dan sort.
    - Keyword digunakan untuk mencari data yang mengandung kata kunci tertentu.
    - Fields digunakan untuk menentukan field mana saja yang akan dicari.
    - Select digunakan untuk menentukan field mana saja yang akan ditampilkan.
    - Limit digunakan untuk menentukan jumlah data yang akan ditampilkan.
    - Page digunakan untuk menentukan halaman data yang akan ditampilkan.
    - Sort digunakan untuk menentukan urutan data yang akan ditampilkan.

    Request Body Example:
    {
        "keyword" : "String",
        "fields" : "String",
        "select" : "String",
        "limit" : Int,
        "page" : Int,
        "sort" : "String",
    }

    Response Body Example:
    Response body dapat menjadi beragam bentuk sesuai dengan select yang diberikan.
    Hasil akan dikembalikan dalam bentuk JSON. Hasil pencarian akan berada pada key "data".
    Isi dari key data hanya akan berisi data yang sesuai dengan select yang diberikan
    dan hanya memiliki kedalaman 1 level.
    '''
    keyword : str = request.keyword.lower()
    fields : list[str] = ["*"] if request.fields == "*" else [item for item in "".join(request.fields.lower().split()).split(",") if "." in item]
    select : list[str] = ["*"] if request.select == "*" else [item for item in "".join(request.select.lower().split()).split(",") if "." in item]
    limit : int = request.limit if request.limit > 0 else 100
    page : int = request.page if request.page > 0 else 1
    sort : str = request.sort.lower() if request.sort.lower() in ["asc", "desc"] else "asc"

    result = await search(db, keyword, fields, select, limit, page, sort)

    response  = BaseResponse(
        status="200 OK",
        message="Data found",
        data=result
    )

    if result is None:
        response.status = "404 Not Found"
        response.message = "Data not found"

    return response


async def search(db: Session, keyword: str, fields: list[str], select: list[str], limit: int, page: int, sort: str) -> List[dict]:
    result = crud.advanced_search(db, keyword, fields, select, limit, page, sort)

    if result is None:
        raise HTTPException(status_code=404, detail="Data not found")

    return result
    