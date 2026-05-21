from kirilltools.errors import base as _err

class BaseDecorateError(_err.BaseExceptionlib): pass
class NotUnlockError(BaseDecorateError): pass

class NerdError(BaseDecorateError): pass
class TrubkaError(NerdError): pass
class LogoutError(NerdError): pass

__all__ = [
    "BaseDecorateError", "NotUnlockError",
    "NerdError", "TrubkaError", "LogoutError"
]