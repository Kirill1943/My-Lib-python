if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    from .FilesAndDir import GenStructures
    from .iter import list_flattening, gen_chank
    from . import decorators, FilesAndDir, iter
    __all__ = [
        "decorators",
        "FilesAndDir",
        'iter'
    ]