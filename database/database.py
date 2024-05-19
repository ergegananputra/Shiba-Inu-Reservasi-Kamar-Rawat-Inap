from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, username, password, host, dbname):
        url = self.__SQLACLHEMY_DATABASE_URL(username, password, host, dbname)
        self.engine = create_engine(url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def __SQLACLHEMY_DATABASE_URL(self, u: str, p: str, h: str, db: str) -> str:
        return f"mysql+pymysql://{u}:{p}@{h}/{db}"

# Database 1
SQLDB_USERNAME_1 = "root"
SQLDB_PASSWORD_1 = ""
SQLDB_HOST_1 = "127.0.0.1"
SQLDB_NAME_1 = "shiba_inu_db"
DBServerWrites = Database(
    SQLDB_USERNAME_1, 
    SQLDB_PASSWORD_1, 
    SQLDB_HOST_1, 
    SQLDB_NAME_1
    )


# Database 2
SQLDB_USERNAME_2 = "root"
SQLDB_PASSWORD_2 = ""
SQLDB_HOST_2 = "127.0.0.1"
SQLDB_NAME_2 = "shiba_inu_db"
DBServerReads = Database(
    SQLDB_USERNAME_2, 
    SQLDB_PASSWORD_2, 
    SQLDB_HOST_2, 
    SQLDB_NAME_2
    )


