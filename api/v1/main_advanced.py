from api.common_bucket import *
from database.database import get_db_reads, get_db_writes 
from crud import main_advanced as crud
import json

from schemas import main_advanced as schemas

router = APIRouter()


@router.get("/api/v1/advanced")
async def get_all_advanced(skip: int = 0, limit: int = 100, db : Session= Depends(get_db_reads)):
    # facilities = crud.get_fasilitas_layanan_kesehatan_all(db, skip=skip, limit=limit)
    # if facilities is None:
    #     raise HTTPException(status_code=404, detail="Facility not found")
    # return facilities
    # TODO: Implement this
    pass

'''
{
    "keyword" : "String",
    "fields" : "String",
    "select" : "String",
    "limit" : "Int",
    "page" : "Int",
    "sort" : "String",
}
'''

@router.get("/api/v1/advanced/search")
async def search_advanced(
        request: schemas.SearchAdvancedRequest,
        db : Session= Depends(get_db_reads)
        ):
    keyword : str = request.keyword.lower()
    fields : list[str] = ["*"] if request.fields == "*" else [item for item in "".join(request.fields.lower().split()).split(",") if "." in item]
    select : list[str] = ["*"] if request.select == "*" else [item for item in "".join(request.select.lower().split()).split(",") if "." in item]
    limit : int = request.limit if request.limit > 0 else 100
    page : int = request.page if request.page > 0 else 1
    sort : str = request.sort.lower() if request.sort in ["asc", "desc"] else "asc"

    result = crud.advanced_search(db, keyword, fields, select, limit, page, sort)
    if result is None:
        raise HTTPException(status_code=404, detail="Data not found")
    else :
        result_json = {
            "status" : "200",
            "message" : "Berhasil mendapatkan data",
            "data" : result
        }

    return result_json
