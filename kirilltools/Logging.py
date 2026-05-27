import rich as _rich
import time as _time
from kirilltools.__advanted import (LOGLEVELCRITICAL, 
                                    LOGLEVELDEBUG, 
                                    LOGLEVELERROR, 
                                    LOGLEVELINFO, 
                                    LOGLEVELWARNING
                                )

def _gettime() -> str:
    t = _time.localtime()
    return f"{t.tm_year}-{t.tm_mon:02d}-{t.tm_mday:02d} {t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}"

def info(message: str, color: bool = False) -> None:
    """
    показывает лог типа INFO

    message: str: какое сообщение показать
    color: bool: использовать ли цвета, 
    ВНИМАНИЕ: для отображения цвета используется rich.print()
    если вы используете обычный print, оставьте опцию color: False
    ведь может случиться конфликт print и rich.print
    """
    if color:
        _rich.print(f'[#00FFFF][ {_gettime()} ] [ INFO ] {message}')
    else:
        print(f'[ {_gettime()} ] [ INFO ] {message}')

def debug(message: str, color: bool = False) -> None:
    """
    показывает лог типа DEBUG

    message: str: какое сообщение показать
    color: bool: использовать ли цвета, 
    ВНИМАНИЕ: для отображения цвета используется rich.print()
    если вы используете обычный print, оставьте опцию color: False
    ведь может случиться конфликт print и rich.print
    """
    if color:
        _rich.print(f'[green][ {_gettime()} ] [ DEBUG ] {message}')
    else:
        print(f'[ {_gettime()} ] [ DEBUG ] {message}')

def warning(message: str, color: bool = False) -> None:
    if color:
        _rich.print(f'[#FFFF00][ {_gettime()} ] [ WARNING ] {message}')
    else:
        print(f'[ {_gettime()} ] [ WARNING ] {message}')

def error(message: str, color: bool = False) -> None:
    if color:
        _rich.print(f'[#FF0000][ {_gettime()} ] [ ERROR ] {message}')
    else:
        print(f'[ {_gettime()} ] [ ERROR ] {message}')

def critical(message: str, color: bool = False) -> None:
    if color:
        _rich.print(f'[#880000][ {_gettime()} ] [ CRITICAL ] {message}')
    else:
        print(f'[ {_gettime()} ] [ CRITICAL ] {message}')


def CustomLog(message: str, levellog: str, color: bool = False):
    """
    показывает полностью кастомный лог
    message: str: сообщение
    levellog: str: тег. например [ CUSTOM ]
    """
    if color:
        _rich.print(f'[#FFFFFF][ {_gettime()} ] [ {levellog.upper()} ] {message}')
    else:
        print(f'[ {_gettime()} ] [ {levellog.upper()} ] {message}')

def Log(message: str, levellog: int, color: bool = False) -> None:
    """
    показывает нужный лог выходя из констант
    LOGLEVEL...
    message: str: сообщение
    levellog: Константа: тег сообщение, по типу [ DEBUG ] [ CRITICAL ]
    color: bool: использовать ли цвета, 
    ВНИМАНИЕ: для отображения цвета используется rich.print()
    если вы используете обычный print, оставьте опцию color: False
    ведь может случиться конфликт print и rich.print
    """
    if levellog == LOGLEVELINFO:
        info(message=message, color=color)
    elif levellog == LOGLEVELDEBUG:
        debug(message=message, color=color)
    elif levellog == LOGLEVELWARNING:
        warning(message=message, color=color)
    elif levellog == LOGLEVELERROR:
        error(message=message, color=color)
    elif levellog == LOGLEVELCRITICAL:
        critical(message=message, color=color)
    else:
        CustomLog(message=message, levellog="CUSTOM", color=color)


__all__ = [
    "Log", "CustomLog",
    "debug", "info", "warning",
    "error", "critical"
]