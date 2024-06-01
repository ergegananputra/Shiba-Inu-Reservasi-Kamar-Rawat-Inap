from schemas.room_schemas import *
from schemas.fleet_kamar import FleetKamar
from schemas.status_kamar import StatusKamar
from schemas.jenis_tempat_tidur import JenisTempatTidur
from schemas.fasilitas_detail_kamar import FasilitasDetailKamar

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
class SearchAdvancedRequest(BaseModel):
    keyword: str
    fields: Optional[str] = "*"
    select: Optional[str] = "*"
    limit: Optional[int] = 100
    page: Optional[int] = 1
    sort: Optional[str] = "asc"
    sam: Optional[str] = "samv1"

class SearchAdvancedResponse(BaseModel):
    id_kasur : Optional[uuid.UUID] = None
    fleet_kamar : Optional[FleetKamar] = None
    status_kamar : Optional[StatusKamar] = None
    jenis_tempat_tidur : Optional[JenisTempatTidur] = None
    fasilitas_detail_kamar : Optional[FasilitasDetailKamar] = None
    tingkat_fasilitas_kesehatan : Optional[str] = None
    biaya_pakai_per_hari : Optional[float] = None
    kode_kamar : Optional[str] = None