from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import users as crud

from schemas.users import UserLogin, Users

router = APIRouter()

"""
FLAGGED BY Erge

Kode ini tidak aman, jangan pernah mengirimkan hashed password atau password ke client.
Kirimkan hanya token yang dihasilkan oleh JWT.

"""

# @router.post("/api/v1/login", response_model=BaseResponse[Users])
# async def get_users_by_username(form_data: UserLogin, db : Session= Depends(get_db_reads)):
#     users = crud.get_user_by_username(db,  username=form_data.username)
#     if not users or not crud.verify_password(form_data.password, users.hashed_password):
#         return BaseResponse(
#             status="404 Not Found",
#             message="Username atau password salah",
#         )
    
#     users.hashed_password = None
    
#     response = BaseResponse(
#         status="200 OK",
#         message="Berhasil login",
#         data=users
#     )

#     return users