from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, str_uniq, str_null_false
from app.model.enums.role import RoleEnum


class User(Base):
    __abstract__ = True
    email: Mapped[str_uniq]
    password: Mapped[str_null_false]
    role: Mapped[RoleEnum]
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)