from kirilltools.errors import iter as err
from kirilltools.errors import math as matherr


def gen_chank(list_: list, size: int) -> list:
    try:
        size = int(size)
        if size <= 0:
            raise err.SizeLessZero("укажи в size число 1 или больше!")
    except (ValueError, TypeError):
        raise matherr.TypesError("Размер чанка (size) должен быть целым числом больше 0")

    if not isinstance(list_, list):
        raise err.NotAListError("В list_ нужно передать именно список")

    return [list_[i:i + size] for i in range(0, len(list_), size)]

def list_flattening(list_: list) -> list:
    if not isinstance(list_, list):
        raise err.NotAListError("В list_ нужно передать именно список")
    result_list = []
    for i in list_:
        if not isinstance(i, list):
            raise err.NotListInListError("функция предназначена для сплющивания списков, а у тебя в списке нету списка")
        else:
            result_list.extend(i)
    return result_list

__all__ = [
    "list_flattening",
    "gen_chank"
]