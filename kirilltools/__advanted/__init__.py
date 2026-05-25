if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    __lazy_modules__ = [
        "kirilltools.__advanted.Logging_valdbares"
    ]
    from . import Logging_valdbares
    from .Logging_valdbares import *
    __all__ = [
        "Logging_valdbares"
    ]