from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import async_session_maker
from app.dto.request.address_create import AddressCreate
from app.dto.request.address_update import AddressUpdate
from app.dto.response.address_response import AddressResponse
from app.repository.address_repository import AddressRepository
from app.service.address_service import AddressService

router = APIRouter(prefix="/addresses", tags=["addresses"])


async def get_service() -> AddressService:
    async with async_session_maker() as session:
        repo = AddressRepository(session)
        return AddressService(repo)


@router.post("/", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
async def create_address(
        address: AddressCreate,
        service: AddressService = Depends(get_service)
):
    return await service.create_address(address)


@router.get("/{address_id}", response_model=Optional[AddressResponse])
async def read_address(
        address_id: int,
        service: AddressService = Depends(get_service)
):
    address = await service.get_address(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@router.get("/", response_model=list[AddressResponse])
async def read_addresses(
        service: AddressService = Depends(get_service)
):
    return await service.get_all_addresses()


@router.put("/{address_id}", response_model=AddressResponse)
async def update_address(
        address_id: int,
        address: AddressUpdate,
        service: AddressService = Depends(get_service)
):
    try:
        return await service.update_address(address_id, address)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(
        address_id: int,
        service: AddressService = Depends(get_service)
):
    deleted = await service.delete_address(address_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"detail": "Address deleted successfully"}
