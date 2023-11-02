from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.models import db_helper
from .crud import (
    _get_all_products,
    _create_product,
    _update_product,
    _delete_product,
)
from .dependencies import product_by_id
from .schemas import Product, ProductCreate, ProductUpdate

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_all_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await _get_all_products(session)


@router.get("/{product_id}", response_model=Product)
async def get_product_by_id(
        product: Product = Depends(product_by_id)
):
    return product


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
        product: ProductCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await _create_product(session, product=product)


@router.put("/{product_id}")
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await _update_product(
        session,
        product=product,
        product_update=product_update
    )


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await _delete_product(
        session=session,
        product=product
    )
