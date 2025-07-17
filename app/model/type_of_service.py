from typing import List

from sqlalchemy.orm import Mapped, relationship

from app.database import *
#from app.model.service_detail import ServiceDetail


class TypeOfService(Base):
    __tablename__ = 'type_of_service'
    id: Mapped[int_pk]
    code: Mapped[str_null_false]
    name: Mapped[str_null_false]

    service_details: Mapped[List["ServiceDetail"]] = relationship(
        back_populates="type",
        cascade="all, delete-orphan"
    )
