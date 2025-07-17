from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, text, Text

from app.database import Base, str_uniq, int_pk, str_null_true, str_null_false
#from app.model.address import Address
#from app.model.connection_request import ConnectionRequest
#from app.model.service_detail import ServiceDetail
#from app.model.service_request import ServiceRequest


class Organization(Base):
    id: Mapped[int_pk]
    full_name: Mapped[str_null_false]
    short_name: Mapped[str_null_true]
    inn: Mapped[str_null_false]
    kpp: Mapped[str_null_false]
    ogrn: Mapped[str_null_false]
    responsible_person_name: Mapped[str_null_true]
    responsible_person_patronymic: Mapped[str_null_true]
    responsible_person_email: Mapped[str_null_true]
    responsible_person_phone_number: Mapped[str_null_true]
    add_info: Mapped[str] = mapped_column(Text, nullable=True)

    # OneToMany связи
    connection_requests: Mapped[List["ConnectionRequest"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan"
    )

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan"
    )

    service_requests: Mapped[List["ServiceRequest"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan"
    )

    service_details: Mapped[List["ServiceDetail"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan"
    )