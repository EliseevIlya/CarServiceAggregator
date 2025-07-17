from typing import List

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Date, Text, ForeignKey
from datetime import date

from app.database import *
from app.model.service_detail import service_request_detail


#from app.model.customer import Customer
#from app.model.organization import Organization
#from app.model.service_detail import ServiceDetail, service_request_detail


class ServiceRequest(Base):
    __tablename__ = 'service_request'
    id: Mapped[int_pk]
    date_service: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())
    add_info: Mapped[str] = mapped_column(Text, nullable=True)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"), nullable=False)
    customer: Mapped["Customer"] = relationship(back_populates="service_requests")

    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"), nullable=False)
    organization: Mapped["Organization"] = relationship(back_populates="service_requests")

    # ManyToMany с ServiceDetail
    service_details: Mapped[List["ServiceDetail"]] = relationship(
        secondary=service_request_detail,
        back_populates="service_requests",
        cascade="save-update, merge"
    )

