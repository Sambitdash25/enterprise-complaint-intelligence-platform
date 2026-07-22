import uuid

from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Prediction(Base):
    """
    ORM model representing AI-generated complaint predictions.
    """

    __tablename__ = "predictions"

    prediction_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        )

    complaint_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("complaints.complaint_id"),
        nullable=False,
        )

    severity_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    root_cause: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    sentiment: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    suggested_resolution: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    explanation: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    confidence_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )