from typing import Optional, List

from app.dto.request.address_create import AddressCreate
from app.dto.request.address_update import AddressUpdate
from app.dto.response.address_response import AddressResponse
from app.repository.address_repository import AddressRepository


class AddressService:
    def __init__(self, repository: AddressRepository):
        self.repository = repository

    async def create_address(self, address: AddressCreate) -> AddressResponse:
        return await self.repository.create(address)

    async def get_address(self, address_id: int) -> Optional[AddressResponse]:
        address = await self.repository.get_by_id(address_id)
        return address if address else None

    async def get_all_addresses(self) -> List[AddressResponse]:
        return await self.repository.get_all()

    async def update_address(self, address_id: int, address: AddressUpdate) -> Optional[AddressResponse]:
        updated = await self.repository.update(address_id, address)
        if not updated:
            raise ValueError(f"Address {address_id} not found")
        return updated

    async def delete_address(self, address_id: int) -> bool:
        return await self.repository.delete(address_id)
