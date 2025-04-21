from contextlib import asynccontextmanager
from datetime import datetime
import os
import sys
sys.path.append(os.path.dirname(__file__)) 

from fastapi import FastAPI, status
from pydantic import BaseModel
import uvicorn


PORT = os.environ.get("PORT")
HOST = os.environ.get("HOST")
DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}
print(PORT, HOST, DEBUG)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup:
    print("Starting up...")

    # Yield back to FastAPI Application:
    yield



app = FastAPI(lifespan=lifespan, debug=DEBUG)

class DummyResponse(BaseModel):
    id: str
    when: datetime


@app.get("/api/dummy")
async def get_dummy() -> DummyResponse:
    return DummyResponse(
        id=str(ObjectId()),
        when=datetime.now(),
    )


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host=HOST, port=PORT, reload=DEBUG)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()