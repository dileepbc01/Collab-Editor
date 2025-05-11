
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from routers import auth,workspace
from fastapi.middleware.cors import CORSMiddleware



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

allow_origins = [
    "http://localhost:3000",
]
app = FastAPI(lifespan=lifespan, docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(
    auth.router,
)   

app.include_router(
    workspace.router
)   



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8080)
