from sqlmodel import SQLModel
from .user import User
from .workspace import Workspace
from .workspace_relation import WorkspaceRelation
# Import any other models here

# This ensures all models are imported when the models package is imported
__all__ = ["User","Workspace","WorkspaceRelation"]  # Add other model names as needed