from sqlmodel import SQLModel, Field, Relationship
import uuid
from datetime import datetime
from .user import User
from .workspace import Workspace    

class WorkspaceRelation(SQLModel, table=True):
    __tablename__ = "workspace_relation"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    user_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    workspace_id: uuid.UUID = Field(foreign_key="workspace.id", nullable=False)
    is_creator: bool = Field(default_factory=False)

    # Relationships
    user: "User" = Relationship(back_populates="workspace_relations")
    workspace: "Workspace" = Relationship(back_populates="relations")
