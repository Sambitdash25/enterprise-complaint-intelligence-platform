from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings

# URL-encode the password to safely handle special characters
password = quote_plus(settings.DATABASE_PASSWORD)

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.DATABASE_USER}:"
    f"{password}@"
    f"{settings.DATABASE_HOST}:"
    f"{settings.DATABASE_PORT}/"
    f"{settings.DATABASE_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)