import uuid

from sqlalchemy import Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Employee(Base):
    """
    ORM model representing an employee who can handle complaints.
    """

    __tablename__ = "employees"

    employee_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    employee_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    department: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    skills: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    workload: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    availability: Mapped[str] = mapped_column(
        String(30),
        default="Available",
        nullable=False,
    )

    experience_level: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )