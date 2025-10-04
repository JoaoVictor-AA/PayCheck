from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.ext.declarative
import psycopg2
BANCO_DE_DADOS_URL = "postgresql://postgres:password@127.0.0.1:5432/meu_banco"


engine = create_engine(BANCO_DE_DADOS_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
