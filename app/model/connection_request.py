from enum import Enum
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, text, Text, Date
from app.database import Base, str_uniq, int_pk, str_null_true, str_null_false
from datetime import date

from app.model.aggregator_specialist import aggregator_specialist_connector_request
#from app.model.aggregator_specialist import AggregatorSpecialist, aggregator_specialist_connector_request
from app.model.enums.status import StatusEnum
#from app.model.organization import Organization


class ConnectionRequest(Base):
    __tablename__ = 'connection_request'
    id: Mapped[int_pk]
    registration_number: Mapped[str_null_false]
    dateBegin: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())
    dateEnd: Mapped[date]
    status: Mapped[StatusEnum]
    add_info: Mapped[str] = mapped_column(Text, nullable=True)

    # ManyToMany с AggregatorSpecialist
    aggregator_specialists: Mapped[List["AggregatorSpecialist"]] = relationship(
        secondary=aggregator_specialist_connector_request,
        back_populates="connection_requests",
        lazy="select"
    )

    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"), nullable=False)
    organization: Mapped["Organization"] = relationship(back_populates="connection_requests")
