from typing import Annotated

from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api_v1.products.crud import _get_product_by_id
from core.models import db_helper, Product


async def product_by_id(
        product_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    product = await _get_product_by_id(session, product_id)
    if product:
        return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
