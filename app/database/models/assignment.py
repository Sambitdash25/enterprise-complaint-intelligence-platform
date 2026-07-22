import uuid
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Assignment(Base):
    """
    ORM model representing complaint assignments.
    """

    __tablename__ = "assignments"

    assignment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    complaint_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("complaints.complaint_id"),
        nullable=False,
    )

    employee_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("employees.employee_id"),
        nullable=False,
    )

    assigned_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    assigned_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    assignment_status: Mapped[str] = mapped_column(
        String(30),
        default="Assigned",
        nullable=False,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )