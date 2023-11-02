from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.models import db_helper, Base
from items.views import router as items_router
from users.views import router as users_router
from core.conflig import settings
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_sum")
async def get_sum(a: int, b: int):
    return {
        "a": a,
        "b": a,
        "sum": a + b,
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=8001)
