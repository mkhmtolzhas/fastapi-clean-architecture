from fastapi import APIRouter, Depends
from src.usecases.domain_usecase import get_domain_usecase, DomainUseCase
from src.schemas.base_schema import ResponseSchema
from src.schemas.domain_schema import DomainCreateSchema, DomainUpdateSchema, DomainReadSchema
from typing import List

router = APIRouter(prefix="/domains", tags=["Domains"])

@router.post("/", response_model=ResponseSchema[DomainReadSchema])
async def create_domain(
    obj: DomainCreateSchema,
    usecase: DomainUseCase = Depends(get_domain_usecase)
) -> ResponseSchema[DomainReadSchema]:
    """
    Create a domain.
    """
    response = await usecase.create(obj)
    return ResponseSchema[DomainReadSchema](
        status="ok",
        message="succes",
        data=response
    )


@router.get("/{id}", response_model=ResponseSchema[DomainReadSchema])
async def get_domain(
    id: int,
    usecase: DomainUseCase = Depends(get_domain_usecase)
) -> ResponseSchema[DomainReadSchema]:
    """
    Get a domain by ID.
    """

    response = await usecase.get_by_id(id)
    return ResponseSchema[DomainReadSchema](
        status="ok",
        message="succes",
        data=response
    )


@router.put("/", response_model=ResponseSchema[DomainReadSchema])
async def update_domain(
    obj: DomainUpdateSchema,
    usecase: DomainUseCase = Depends(get_domain_usecase)
) -> ResponseSchema[DomainReadSchema]:
    """
    Update a domain.
    """
    response = await usecase.update(obj)
    return ResponseSchema[DomainReadSchema](
        status="ok",
        message="succes",
        data=response
    )


@router.delete("/{id}", response_model=ResponseSchema[bool])
async def delete_domain(
    id: int,
    usecase: DomainUseCase = Depends(get_domain_usecase)
) -> ResponseSchema[bool]:
    """
    Delete a domain by ID.
    """
    response = await usecase.delete_by_id(id)
    return ResponseSchema[bool](
        status="ok",
        message="succes",
        data=response
    )


@router.get("/", response_model=ResponseSchema[List[DomainReadSchema]])
async def list_domains(
    page: int = 1,
    limit: int = 10,
    usecase: DomainUseCase = Depends(get_domain_usecase)
) -> ResponseSchema[List[DomainReadSchema]]:
    """
    List domains.
    """
    response = await usecase.list(page, limit)
    return ResponseSchema[List[DomainReadSchema]](
        status="ok",
        message="succes",
        data=response
    )

