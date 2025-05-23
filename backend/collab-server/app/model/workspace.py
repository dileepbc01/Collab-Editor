from sqlmodel import SQLModel, Field


class BaseWorkspace(SQLModel):
    name: str = Field(index=True, unique=True, nullable=False)
    description: str = Field(nullable=False)
    website: str = Field(nullable=False)
    

class CreateWorkspace(BaseWorkspace):
    pass