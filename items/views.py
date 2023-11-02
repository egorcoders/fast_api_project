from typing import Annotated

from fastapi import Path, APIRouter, HTTPException

from data import items
from items.schemas import Item

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
async def get_all_items():
    return items


@router.get("/{item_id}")
async def get_item_by_id(item_id: Annotated[int, Path(ge=1, le=100)]):
    try:
        return [a for a in items if a["id"] == item_id]
    except Exception:
        raise HTTPException(status_code=404, detail="No such item")


@router.post("/")
async def create_item(item: Item):
    items.append(item.model_dump())
    return item.model_dump()
