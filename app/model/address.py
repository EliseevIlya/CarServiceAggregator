from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, text, Text

from app.database import Base, str_uniq, int_pk, str_null_true
from app.model.enums.address_type import AddressTypeEnum
#from app.model.organization import Organization


class Address(Base):
    id: Mapped[int_pk]
    address_type: Mapped[AddressTypeEnum]
    subject_name: Mapped[str_null_true]
    city_name: Mapped[str_null_true]
    street_name: Mapped[str_null_true]
    house_number: Mapped[str]
    add_info: Mapped[str] = mapped_column(Text, nullable=True)

    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"), nullable=False)
    organization: Mapped["Organization"] = relationship(back_populates="addresses")