from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

env = os.environ
ACCESS_EXPIRES = timedelta(hours=1)

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{}:{}@{}/{}".format(env['User_Postg'], env['Password_Postg'], env['Host_Postg'], env['dbName_Postg'])

engine = create_engine( SQLALCHEMY_DATABASE_URL, client_encoding="utf8")

#jwt_redis_blocklist = redis.StrictRedis(
#    host=env['Host_redis'], port=env['Port_redis'], db=env['dbName_redis'], decode_responses=True
#)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#docker run --restart=always --name dbMedical --network=postgres-network -e "POSTGRES_USER=medicalAppoiment" -e "POSTGRES_PASSWORD=medical123" -e "POSTGRES_DB=medical" -p 5433:5433 -v pgdata:/var/lib/postgresql/data postgres -d postgres
