if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    __lazy_modules__ = [
        "kirilltools.errors.base", "kirilltools.errors.cipherError", 
        "kirilltools.errors.decorators", "kirilltools.errors.FilesAndDir", 
        "kirilltools.errors.iter", "kirilltools.errors.math", "kirilltools.errors.Wifi"
    ]
    from .base import *
    from . import base, cipherError, decorators, FilesAndDir, iter, Wifi
    __all__ = [
        "base", "cipherError", "decorators", "FilesAndDir" , "iter", "math", "Wifi"
    ]