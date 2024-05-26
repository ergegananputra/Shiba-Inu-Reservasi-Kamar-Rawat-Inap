from sqlalchemy.orm import Session
from uuid import UUID

import models.Users
import models.Users
import schemas.users
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()

def create_user(db: Session, user: schemas.users):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.Users(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)