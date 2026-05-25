if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    __lazy_modules__ = ["kirilltools.internet.check"]
    from .check import *
    from . import check
    __all__ = [
        'check'
    ]