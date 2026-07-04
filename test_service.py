from services.workspace_service import WorkspaceService

workspace = WorkspaceService.create_workspace(
    name="Chemistry Notes",
    location="E:/AcademicOS Test"
)

print(workspace)