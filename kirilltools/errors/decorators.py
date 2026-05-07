from kirilltools.errors import base as err

class BaseDecorateError(err.BaseExceptionlib): pass
class NotUnlockError(BaseDecorateError): pass

class NerdError(BaseDecorateError): pass
class TrubkaError(NerdError): pass
class LogoutError(NerdError): pass