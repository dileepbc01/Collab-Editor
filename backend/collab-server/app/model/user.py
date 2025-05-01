from sqlmodel import SQLModel, Field




class BaseUser(SqlModel):
    email: str = Field(index=True, unique=True, nullable=False)
    fullname: str = Field( nullable=False)