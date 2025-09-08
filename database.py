from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (apne MySQL ka username aur password yaha dalo)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Sanket@9022@localhost/vibeosys_db"

# Engine banate hain
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal for DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
