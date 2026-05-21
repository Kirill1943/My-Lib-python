import kirilltools.errors.base as _err

class IterError(_err.BaseExceptionlib): pass
class NotAListError(IterError): pass
class SizeLessZero(IterError): pass
class NotListInListError(IterError): pass

__all__ = [
    "IterError", "NotAListError",
    "SizeLessZero", "NotListInListError"
]