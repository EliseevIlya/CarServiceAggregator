from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text

from app.database import int_pk, str_null_false, str_null_true
#from app.model.service_request import ServiceRequest
from app.model.user import User


class Customer(User):
    id: Mapped[int_pk]
    surname: Mapped[str_null_false]
    name: Mapped[str_null_false]
    patronymic: Mapped[str_null_true]
    phone_number: Mapped[str_null_true]
    add_info: Mapped[str] = mapped_column(Text, nullable=True)

    # OneToMany с ServiceRequest
    service_requests: Mapped[List["ServiceRequest"]] = relationship(
        back_populates="customer",
        cascade="all, delete-orphan"
    )
