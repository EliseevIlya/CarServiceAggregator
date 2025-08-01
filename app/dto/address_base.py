from typing import Optional
from pydantic import BaseModel

from app.model.enums.address_type import AddressTypeEnum


class AddressBase(BaseModel):
    address_type: AddressTypeEnum
    subject_name: Optional[str] = None
    city_name: Optional[str] = None
    street_name: Optional[str] = None
    house_number: str
    add_info: Optional[str] = None
    organization_id: int
