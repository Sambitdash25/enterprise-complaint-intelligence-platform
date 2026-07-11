from datetime import datetime
from sqlalchemy import DateTime,String,Text 
from sqlalchemy.orm import Mapped,mapped_column

from app.database.base import Base


class Complaint(Base):
     """
    ORM model representing a customer complaint.
    """
     
     
     __tablename__ = "complaints"
     complaint_id: Mapped(str) = mapped_column(
          String(36),
          primary_key = True,
     )

     customer_id: Mapped(str) = mapped_column(
          String(50),
          nullable= False,
     )

     complaint_text: Mapped[str] = mapped_column(
         Text,
         nullable=False,
     )

     source: Mapped[str] = mapped_column(
         String(50),
         nullable=False,
     )

     language: Mapped[str] = mapped_column(
         String(30),
         nullable=False,
     )

     status: Mapped[str] = mapped_column(
         String(30),
         nullable=False,
     )

     external_reference: Mapped[str | None] = mapped_column(
         String(100),
         nullable=True,
     )

     created_at: Mapped[datetime] = mapped_column(
         DateTime,
         default=datetime.utcnow,
         nullable=False,
     )

     updated_at: Mapped[datetime] = mapped_column(
         DateTime,
         default=datetime.utcnow,
         onupdate=datetime.utcnow,
         nullable=False,
     )
