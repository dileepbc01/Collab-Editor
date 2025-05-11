from fastapi import APIRouter,Depends
from app.schema.user import User
from app.utils.get_current_user import get_current_user
from app.model.workspace import CreateWorkspace
from app.schema.workspace import Workspace
from app.schema.workspace_relation import WorkspaceRelation
from app.dependencies.database import SessionDep
from sqlmodel import select


router = APIRouter(
    prefix="/workspace",
    tags=["workspace"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_user_workspaces(
    db: SessionDep,
    current_user: User = Depends(get_current_user)
):
    result = await db.exec(
        select(Workspace, WorkspaceRelation)
        .join(Workspace, WorkspaceRelation.workspace_id == Workspace.id)
        .where(WorkspaceRelation.user_id == current_user.id)
    )
    response = [
        {
            "workspace": workspace,
            "relation": relation
        }
        for workspace, relation in result.all()
    ]
    return {"workspaces": response}


@router.post("/share")
async def share_workspace(
    workspace_id: str,
    user_id: str,
    db: SessionDep,
    current_user: User = Depends(get_current_user),
):
    # Check if the workspace exists
    workspace = await db.get(Workspace, workspace_id)
    if not workspace:
        return {"error": "Workspace not found"}
    if not workspace.created_by==current_user.id:
        return {"error": "You are not the creator of this workspace"}
    user = await db.get(User, user_id)
    if not user:
        return {"error": "User not found"}
    # Check if the user exists
    user = await db.get(WorkspaceRelation, user_id)
    if user:
        return {"error": "User already has access to this workspace"}

    # Create a new relation
    relation = WorkspaceRelation(
        is_creator=False,
        user_id=user_id,
        workspace_id=workspace_id
    )

    # Add the relation to the database
    db.add(relation)
    await db.commit()
    await db.refresh(relation)

    return {"message": "Workspace shared successfully"}


@router.post("/")
async def create_workspace(
    createWorkspaceDto: CreateWorkspace,
    db: SessionDep,
    current_user: User = Depends(get_current_user),
):
    # Create workspace
    new_workspace = Workspace(
        name=createWorkspaceDto.name,
        description=createWorkspaceDto.description,
        created_by=current_user.id,
        website=createWorkspaceDto.website,
    )

    # Create relationship and link to workspace
    workspace_relation = WorkspaceRelation(
        is_creator=True,
        user_id=current_user.id
    )
    new_workspace.relations.append(workspace_relation)

    # Add only workspace; relation is added via relationship
    db.add(new_workspace)
    await db.commit()
    await db.refresh(new_workspace)

    return {"workspace": new_workspace}
