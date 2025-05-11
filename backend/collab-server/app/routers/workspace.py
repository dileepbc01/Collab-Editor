from fastapi import APIRouter

router = APIRouter(
    prefix="/workspace",
    tags=["workspace"],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
def get_userWorkspaces():
    return []

@router.post("/")
def createWorkspace():
    return {}