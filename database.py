from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)

"connects to db"
def create_db_and_tables():
    "connects to db"
    SQLModel.metadata.create_all(engine)
    return "database connected"
