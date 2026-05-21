import kirilltools.errors.base as baseerr

class MathError(baseerr.BaseExceptionlib): pass
class TypesError(MathError): pass
class NumOwerflowError(MathError): pass

__all__ = [
    "MathError",
    "TypesError",
    "NumOwerflowError"
]