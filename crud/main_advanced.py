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
__field_convertion = lambda table, field: f"{__attributes_map[table]}.{field}" if table in __attributes_map else ""



def get_facility_free_space(
        db: Session, 
        keyword: str, 
        limit: int, 
        page: int, 
        sort: str
        ) :

    sql = text(f"""
        SELECT flk.id, flk.nama, flk.alamat, flk.tipe, 
            COUNT(CASE WHEN sk.status = 'kosong' THEN 1 END) as 'tersedia', 
            COUNT(CASE WHEN sk.status = 'terpakai' THEN 1 END) as 'terpakai',
            COUNT(sk.id) as 'total kamar'
        FROM kasur as k
        JOIN fleet_kamar as fkr ON k.fk_fkr = fkr.id
        JOIN fasilitas_layanan_kesehatan as flk ON fkr.fk_flk = flk.id
        JOIN status_kamar as sk ON k.fk_sk = sk.id
        JOIN jenis_tempat_tidur as jtt ON k.fk_jtt = jtt.id
        JOIN fasilitas_detail_kamar as fdk ON k.fk_fdk = fdk.id
        JOIN pendingin_ruangan as fpr ON fdk.fk_fpr = fpr.id
        WHERE LOWER(flk.nama) LIKE LOWER(:keyword)
        GROUP BY flk.id
        ORDER BY flk.nama {sort}
        LIMIT :limit OFFSET :offset
    """)

    try:
        result = db.execute(sql, {
            "limit": limit,
            "offset": (page - 1) * limit,
            "keyword": f"%{keyword}%"
        })

    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError while executing advanced search: {e} \n\nSQL: {sql}")
        result = None

    column_names = result.keys()
    rows = result.fetchall()

    dict_rows = [dict(zip(column_names, row)) for row in rows]

    return dict_rows
    

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


    item_spesific = lambda table, field: f"LOWER({__field_convertion(table, field)}) LIKE LOWER(:keyword)"
    where_clause = " OR ".join([item_spesific(*item.split(".")[:2]) for item in fields if item != ""])

    select_clause = ", ".join([__field_convertion(*item.split(".")[:2]) for item in select if item != ""]) if select != ["*"] else "*"
    select_clause = select_clause if select_clause != "" else "*"

    order_by_clause = ', '.join(f"{__field_convertion(*field.split("."))} {sort}" for field in fields)

    sql = text(
        f"""
        SELECT {select_clause}
        FROM kasur as k
        JOIN fleet_kamar as fkr ON k.fk_fkr = fkr.id
        JOIN fasilitas_layanan_kesehatan as flk ON fkr.fk_flk = flk.id
        JOIN status_kamar as sk ON k.fk_sk = sk.id
        JOIN jenis_tempat_tidur as jtt ON k.fk_jtt = jtt.id
        JOIN fasilitas_detail_kamar as fdk ON k.fk_fdk = fdk.id
        JOIN pendingin_ruangan as fpr ON fdk.fk_fpr = fpr.id
        WHERE {where_clause}
        ORDER BY {order_by_clause}
        LIMIT :limit OFFSET :offset
        """
    )

    try:
        result = db.execute(sql, {
            "keyword": f"%{keyword}%",
            "limit": limit,
            "offset": (page - 1) * limit
        })

        
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError while executing advanced search: {e} \n\nSQL: {sql}")
        result = None

        return result
    
    column_names = result.keys()
    rows = result.fetchall()

    dict_rows = [dict(zip(column_names, row)) for row in rows]

    return dict_rows