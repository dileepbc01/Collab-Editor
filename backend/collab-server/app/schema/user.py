from sqlmodel import  Field, Relationship
from app.model.user import BaseUser
import uuid
from typing import List

class User(BaseUser, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    password_hash: str = Field(nullable=False)

    # Relationship to WorkspaceRelation
    workspace_relations: List["WorkspaceRelation"] = Relationship(back_populates="user")

