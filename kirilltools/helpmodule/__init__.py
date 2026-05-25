if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    __lazy_modules__ = [
        "kirilltools.helpmodule.basefunc", "kirilltools.helpmodule.loops_and_func",
        "kirilltools.helpmodule.OOP_tryexcept", "kirilltools.helpmodule.OpenAndModule",
        "kirilltools.helpmodule.CreateModules"
    ]
    from .CreateModules import *
    from . import basefunc, loops_and_func, OOP_tryexcept, OpenAndModule, CreateModules
    __all__ = [
        "basefunc",
        "loops_and_func",
        "OOP_tryexcept",
        "OpenAndModule",
        "CreateModules"
    ]