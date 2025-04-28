from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from . import Base  # Assuming a base class exists

class Workspace(Base):
    __tablename__ = "workspace"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)

    # Relationships
    created_by_user = relationship("User", back_populates="workspaces")
    workspace_teams = relationship("WorkspaceTeam", back_populates="workspace")