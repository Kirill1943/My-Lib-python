import kirilltools.errors.base as baseerr

class CipherError(baseerr.BaseExceptionlib): pass
class KeyFormatError(CipherError): pass