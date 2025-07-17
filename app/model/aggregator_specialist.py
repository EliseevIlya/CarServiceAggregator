from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Table, Column, Integer

from app.database import Base, str_uniq, int_pk, str_null_true, str_null_false
#from app.model.connection_request import ConnectionRequest
from app.model.organization import Organization
from app.model.user import User

# ManyToMany join-таблица для AggregatorSpecialist <-> ConnectionRequest
aggregator_specialist_connector_request = Table(
    "aggregator_specialist_connector_request",
    Base.metadata,
    Column("aggregator_specialists_id", Integer, ForeignKey("aggregator_specialist.id")),
    Column("connection_request_id", Integer, ForeignKey("connection_request.id"))
)


class AggregatorSpecialist(User):
    __tablename__ = 'aggregator_specialist'
    id: Mapped[int_pk]
    surname: Mapped[str_null_false]
    name: Mapped[str_null_false]
    patronymic: Mapped[str_null_true]
    department: Mapped[str_null_true]
    position: Mapped[str_null_true]
    phone_number: Mapped[str_null_true]
    add_info: Mapped[str] = mapped_column(Text, nullable=True)



    # ManyToMany с ConnectionRequest
    connection_requests: Mapped[List["ConnectionRequest"]] = relationship(
        secondary=aggregator_specialist_connector_request,
        back_populates="aggregator_specialists",
        cascade="save-update, merge",
        lazy="select"
    )
