import kirilltools.errors.base as err

class IterError(err.BaseExceptionlib): pass
class NotAListError(IterError): pass
class SizeLessZero(IterError): pass
class NotListInListError(IterError): pass