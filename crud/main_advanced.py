from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from uuid import UUID
# import models.fasilitas_layanan_kesehatan as models
import schemas.main_advanced as schemas

from utils.logger import logger

__attributes_map : dict[str, str] = {
    "kasur": "k",
    "fleet_kamar": "fkr",
    "fasilitas_layanan_kesehatan": "flk",
    "status_kamar": "sk",
    "jenis_tempat_tidur": "jtt",
    "fasilitas_detail_kamar": "fdk",
    "pendingin_ruangan": "fpr"

}

def advanced_search(
        db: Session, 
        keyword: str, 
        fields: list[str], 
        select: list[str], 
        limit: int, 
        page: int, 
        sort: str
        ) :
    '''
    Advanced search function
    keyword, fileds, and select is not clean and vulnerable to SQL Injection.
    Make sure to sanitize the input before using this function.
    '''

    if fields == ["*"]:
        fields = [
            "kasur.kode_kamar", "kasur.tingkat_fasilitas_kesehatan",
            "jenis_tempat_tidur.jenis_tempat_tidur", 
            "fleet_kamar.nama", "fleet_kamar.jenis_kamar",
            "fasilitas_layanan_kesehatan.nama", "fasilitas_layanan_kesehatan.alamat",
            ]
    elif len(fields) == 1:
        fields = [f"{__attributes_map[table]}.{field}" for table, field in [item.split(".")[:2] for item in fields if item != ""]]

    field_convertion = lambda table, field: f"{__attributes_map[table]}.{field}" if table in __attributes_map else ""

    item_spesific = lambda table, field: f"{field_convertion(table, field)} LIKE :keyword"
    where_clause = " OR ".join([item_spesific(*item.split(".")[:2]) for item in fields if item != ""])

    select_clause = ", ".join([field_convertion(*item.split(".")[:2]) for item in select if item != ""]) if select != ["*"] else "*"
    
    if len(select) == 1:
        select_clause = f"{field_convertion(*select[0].split(".")[:2])}"

    sql = text(
        f"""
        SELECT {select_clause}
        FROM jenis_tempat_tidur as jtt
        
        WHERE {where_clause}
        ORDER BY :fields :sort
        LIMIT :limit OFFSET :offset
        """
    )

    try:
        result = db.execute(sql, {
            "keyword": f"%{keyword}%",
            "fields": fields,
            "sort": sort,
            "limit": limit,
            "offset": (page - 1) * limit
        })
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError while executing advanced search: {e}")
        result = None
    

    return result.fetchall()