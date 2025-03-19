import os
import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()

DATABASE_URL = os.environ.get("DATABASE_URL")
print(DATABASE_URL)
if DATABASE_URL is None:
    raise ValueError("Database Url is not set or is unaccessible")


url_table = sqlalchemy.Table(
    "urls",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("original_url", sqlalchemy.String(), nullable=False),
    sqlalchemy.Column("short_url", sqlalchemy.String(), nullable=False, unique=True),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
database = databases.Database(DATABASE_URL)

async def connect_db():
    """Connecting Database on startup"""
    return await database.connect()

async def disconnect_db():
    """Disconnecting Database on shutdown"""
    return await database.disconnect()

def create_tables():
    """Creating tables in the database, if they do not exist"""
    metadata.create_all(engine)
    print("Created successfully")
# create_tables()