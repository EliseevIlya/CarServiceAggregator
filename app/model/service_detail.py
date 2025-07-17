from typing import List

from sqlalchemy import Text, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.database import *
#from app.model.organization import Organization
#from app.model.service_request import ServiceRequest
#from app.model.type_of_service import TypeOfService

# ManyToMany join-таблица для ServiceRequest <-> ServiceDetail
service_request_detail = Table(
    "service_request_detail",
    Base.metadata,
    Column("service_request_id", Integer, ForeignKey("service_request.id")),
    Column("service_detail_id", Integer, ForeignKey("service_detail.id"))
)

class ServiceDetail(Base):
    __tablename__ = 'service_detail'
    id: Mapped[int_pk]
    code: Mapped[str_null_false]
    name: Mapped[str_null_false]
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    add_info: Mapped[str] = mapped_column(Text, nullable=True)

    type_id: Mapped[int] = mapped_column(ForeignKey("type_of_service.id"), nullable=False)
    type: Mapped["TypeOfService"] = relationship(back_populates="service_details")

    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"), nullable=False)
    organization: Mapped["Organization"] = relationship(back_populates="service_details")

    # ManyToMany с ServiceRequest
    service_requests: Mapped[List["ServiceRequest"]] = relationship(
        secondary=service_request_detail,
        back_populates="service_details",
        lazy="select"
    )

