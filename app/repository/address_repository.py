from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dto.request.address_create import AddressCreate
from app.dto.request.address_update import AddressUpdate
from app.dto.response.address_response import AddressResponse
from app.model.address import Address


class AddressRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, address: AddressCreate) -> AddressResponse:
        db_address = Address(**address.model_dump())
        self.session.add(db_address)
        await self.session.commit()
        await self.session.refresh(db_address)
        return AddressResponse.model_validate(db_address)

    async def get_by_id(self, address_id: int) -> Optional[AddressResponse]:
        result = await self.session.execute(
            select(Address).where(Address.id == address_id)
        )
        db_address = result.scalar_one_or_none()
        if db_address:
            return AddressResponse.model_validate(db_address)
        return None

    async def get_all(self) -> list[AddressResponse]:
        result = await self.session.execute(select(Address))
        db_addresses = result.scalars().all()
        return [AddressResponse.model_validate(addr) for addr in db_addresses]

    async def update(self, address_id: int, address: AddressUpdate) -> Optional[AddressResponse]:
        db_address = await self.get_by_id(address_id)
        if not db_address:
            return None
        for key, value in address.model_dump(exclude_unset=True).items():
            setattr(db_address, key, value)
        await self.session.commit()
        await self.session.refresh(db_address)
        return AddressResponse.model_validate(db_address)

    async def delete(self, address_id: int) -> bool:
        db_address = await self.get_by_id(address_id)
        if not db_address:
            return False
        await self.session.delete(db_address)
        await self.session.commit()
        return True
