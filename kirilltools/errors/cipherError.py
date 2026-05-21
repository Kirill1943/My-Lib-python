import kirilltools.errors.base as _baseerr

class CipherError(_baseerr.BaseExceptionlib): pass
class KeyFormatError(CipherError): pass

__all__ = [
    "CipherError",
    "KeyFormatError"
]