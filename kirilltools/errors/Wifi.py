from kirilltools.errors.base import BaseExceptionlib

class ConnectError(BaseExceptionlib): pass
class HttpsError(BaseExceptionlib): pass

__all__ = [
    'ConnectError',
    "HttpsError"
]