if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    from .CreateModules import *
    from . import *
    __all__ = [
        "basefunc",
        "loops_and_func",
        "OOP_tryexcept",
        "OpenAndModule",
        "CreateModules"
    ]