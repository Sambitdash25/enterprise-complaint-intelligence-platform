import uuid
from datetime import datetime, UTC

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID

from app.database.base import Base


class Complaint(Base):
     """
    ORM model representing a customer complaint.
    """
     
     
     __tablename__ = "complaints"
     complaint_id: Mapped[uuid.UUID] = mapped_column(
          UUID(as_uuid=True),
          primary_key=True,
          default=uuid.uuid4,
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
          DateTime(timezone=True),
          default=lambda: datetime.now(UTC),
          nullable=False,
          )

     updated_at: Mapped[datetime] = mapped_column(
          DateTime(timezone=True),
          default=lambda: datetime.now(UTC),
          onupdate=lambda: datetime.now(UTC),
          nullable=False,
          )
