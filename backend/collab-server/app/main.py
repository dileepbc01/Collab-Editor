from fastapi import FastAPI

import logging
import sys
from contextlib import asynccontextmanager
from app.config import settings

# from app.api.routers.users import router as users_router
# from app.database import sessionmanager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG if settings.log_level == "DEBUG" else logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    # if sessionmanager._engine is not None:
    #     # Close the DB connection
    #     await sessionmanager.close()


app = FastAPI(lifespan=lifespan,  docs_url="/api/docs")


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Routers
# app.include_router(users_router)
