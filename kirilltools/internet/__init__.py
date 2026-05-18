if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    from .check import *
    from . import check
    __all__ = [
        'check'
    ]