from app.dto.address_base import AddressBase


class AddressResponse(AddressBase):
    id: int

    class Config:
        from_attributes = True
