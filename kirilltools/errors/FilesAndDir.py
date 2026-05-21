import kirilltools.errors.base as _err

class BaseFilesError(_err.BaseExceptionlib): pass
class BaseDirError(_err.BaseExceptionlib): pass

class NotPathError(BaseDirError): pass

class IsFileError(BaseFilesError): pass

__all__ = [
    "BaseFilesError", "IsFileError",
    "BaseDirError", "NotPathError"
]