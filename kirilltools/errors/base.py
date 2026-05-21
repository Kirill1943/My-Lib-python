

class BaseExceptionlib(Exception): pass
class ForceInterruptionError(BaseExceptionlib): pass
class RunInitError(BaseExceptionlib): pass
class MemoryEndError(BaseExceptionlib): pass

__all__ = [
    "BaseExceptionlib", "MemoryEndError",
    "ForceInterruptionError", "RunInitError"
]