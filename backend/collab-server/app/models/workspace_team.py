from sqlalchemy import Column, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from . import Base  # Assuming a base class exists

class WorkspaceTeam(Base):
    __tablename__ = "workspace_team"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    is_creator = Column(Boolean, default=False, nullable=False)
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspace.id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="workspace_teams")
    workspace = relationship("Workspace", back_populates="workspace_teams")