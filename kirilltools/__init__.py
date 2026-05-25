if __name__ == "__main__":
    import kirilltools.errors.base
    raise kirilltools.errors.base.RunInitError('не вызывать напрямую!!')
else:
    __lazy_modules__ = [
    "kirilltools.taskmgr", "kirilltools.Math", 
    "kirilltools.Logging", "kirilltools.Utils", 
    "kirilltools.internet", "kirilltools.helpmodule", 
    "kirilltools.errors", "kirilltools.__advanted"
    ]
    from . import taskmgr, Math, Logging, Utils, internet, helpmodule, errors, __advanted