if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    __lazy_modules__ = [
        "kirilltools.Utils.FilesAndDir", "kirilltools.Utils.decorators",
        "kirilltools.Utils.iter", "kirilltools.Utils.typedata"
    ]
    from .FilesAndDir import *
    from .typedata import *
    from .iter import *
    from . import decorators, FilesAndDir, iter, typedata
    __all__ = [
        "decorators",
        "FilesAndDir",
        'iter',
        "typedata"
    ]