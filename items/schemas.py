from typing import Annotated

from fastapi import Path
from pydantic import BaseModel


class Item(BaseModel):
    id: Annotated[int, Path(ge=1, le=100)]
    name: str

