from app.database.base import Base
from app.database.models import *
from app.database.session import engine

def init_db() -> None:
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)



if __name__ == "__main__":
    init_db()
    print("Database tables created successfully!")