from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: Annotated[int, Field(ge=1, le=100)]
    name: Annotated[str, MinLen(5), MaxLen(100)]
    age: Annotated[int, Field(ge=1, le=100)]
    email: EmailStr

