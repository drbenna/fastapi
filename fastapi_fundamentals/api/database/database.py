from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi.db"
#SQLALCHEMY_DATABASE_URL = "mysql://apdmin:password@fastapiinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com/fastapi"
SQLALCHEMY_DATABASE_URL = "mysql://admin:fastapi-fundamentals@fastapi-fundamentals.cv4j5avpdfdb.us-east-1.rds.amazonaws.com"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()