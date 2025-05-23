from sqlmodel import SQLModel, Field




class BaseUser(SQLModel):
    email: str = Field(index=True, unique=True, nullable=False)
    fullname: str = Field( nullable=False)
    
class CreateUser(BaseUser):
    password: str = Field(nullable=False)