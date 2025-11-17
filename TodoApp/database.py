from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#cloud postgres setup
SQLALCHEMY_DATABASE_URL = "postgresql://avnadmin:AVNS_cT41ONPcQKztgdv0WnG@pg-e96814a-deploy-postgres-db.h.aivencloud.com:11233/defaultdb?sslmode=require"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#sqlite setup
#SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()