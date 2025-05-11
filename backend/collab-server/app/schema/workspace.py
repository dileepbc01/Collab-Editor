from app.model.workspace import BaseWorkspace
import uuid
from sqlmodel import Field, Relationship
from datetime import datetime
from typing import List

class Workspace(BaseWorkspace, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_by: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)

    # Relationship to WorkspaceRelation
    relations: List["WorkspaceRelation"] = Relationship(back_populates="workspace")
