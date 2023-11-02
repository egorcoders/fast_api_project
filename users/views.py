from typing import Annotated

from fastapi import Path, APIRouter, HTTPException

from data import users
from users.schemas import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_all_users():
    return users


@router.get("/{user_id}")
async def get_item_by_id(user_id: Annotated[int, Path(ge=1, le=100)]):
    try:
        return [a for a in users if a["id"] == user_id]
    except Exception:
        raise HTTPException(status_code=404, detail="No such item")


@router.post("/")
async def create_item(item: User):
    users.append(item.model_dump())
    return item.model_dump()
