from api.common_bucket import *
from database.database import get_db_reads, get_db_writes
from crud import users as crud

from schemas.users import UserLogin, Users

router = APIRouter()

@router.post("/api/v1/login", response_model=Users)
async def get_users_by_username(form_data: UserLogin, db : Session= Depends(get_db_reads)):
    users = crud.get_user_by_username(db,  username=form_data.username)
    if not users or not crud.verify_password(form_data.password, users.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return users