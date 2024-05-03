from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./exper_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# SQLALCHEMY_DATABASE_URL = "postgresql://uni:uni12298@localhost:5432/database_uni"
SQLALCHEMY_DATABASE_URL = "postgresql://root:NwuafSFfgiXVniqYEcSwDjt2@postgres:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()