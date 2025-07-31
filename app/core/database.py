import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.alloydb.connector import Connector
from dotenv import load_dotenv

load_dotenv()

# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        os.environ["ALLOYDB_CONNECTION_NAME"],
        "pg8000",
        user=os.environ["ALLOYDB_USER"],
        password=os.environ["ALLOYDB_PASSWORD"],
        db=os.environ["ALLOYDB_DB"],
        ip_type="PUBLIC"
    )
    return conn

# create SQLAlchemy engine
engine = create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
