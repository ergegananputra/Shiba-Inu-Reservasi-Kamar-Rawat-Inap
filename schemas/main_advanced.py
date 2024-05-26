from schemas.room_schemas import *
from typing import List
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