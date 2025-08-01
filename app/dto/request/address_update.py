from typing import Optional

from app.dto.address_base import AddressBase
from app.model.enums.address_type import AddressTypeEnum


class AddressUpdate(AddressBase):
    address_type: Optional[AddressTypeEnum] = None
    house_number: Optional[str] = None
    organization_id: Optional[int] = None
