import kirilltools.errors.base as err

class BaseFilesError(err.BaseExceptionlib): pass
class BaseDirError(err.BaseExceptionlib): pass

class NotPathError(BaseDirError): pass

class IsFileError(BaseFilesError): pass