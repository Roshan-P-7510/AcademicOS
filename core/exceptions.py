class AcademicOSError(Exception):
    """Base exception for AcademicOS."""
    pass


class WorkspaceError(AcademicOSError):
    """Raised for workspace-related errors."""
    pass


class DatabaseError(AcademicOSError):
    """Raised for database-related errors."""
    pass