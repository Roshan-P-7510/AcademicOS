from storage.filesystem import FileSystem

workspace = FileSystem.create_workspace(
    parent_folder="E:/AcademicOS Test",
    workspace_name="Physics Notes"
)

print(workspace)