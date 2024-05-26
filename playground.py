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
        fields: list[str], 
        select: list[str], 
        sort: str = "asc"
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

    field_convertion = lambda table, field: f"{__attributes_map[table]}.{field}" if table in __attributes_map else ""

    item_spesific = lambda table, field: f"LOWER({field_convertion(table, field)}) LIKE LOWER(:keyword)"
    where_clause = " OR ".join([item_spesific(*item.split(".")[:2]) for item in fields if item != ""])

    select_clause = ", ".join([field_convertion(*item.split(".")[:2]) for item in select if item != ""]) if select != ["*"] else "*"
  
    order_by_clause = ', '.join(f"{field_convertion(*field.split("."))} {sort}" for field in fields)

    sql = f"""
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
    
    print(sql)
    

if __name__ == "__main__":
    advanced_search(
        fields=["kasur.kode_kamar", "fleet_kamar.nama"],
        select=["kasur.kode_kamar", "fleet_kamar.nama"]
    )