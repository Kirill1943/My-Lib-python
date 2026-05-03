from kirilltools.errors.math import TypesError
import kirilltools.errors.cipherError as err

def Caesar_cipher(text: str, next: int = 1024) -> str:
    """
    распостраненный шифр цезаря который сдвигает 
    каждую букву на несколько позиций вперед в unicode
    """
    try:
        next = int(next)
    except TypeError:
        raise TypesError("ты ввел не число в поле next!") from None
    return_text = ''
    for i in text:
        i = chr(ord(i) + next)
        return_text = return_text + str(i)
    return return_text

def custom_cipher(text: str, key: list) -> dict:
    """
    это функция позволяющая зашифровать своим ключом
    сообщение. работает это по принципу списков в списке, пример:
    text = abc
    key = [["a", "b"], ["c", "b"]]
    вернет bbb
    """
    try:
        if not isinstance(key, list):
            raise err.KeyFormatError("Ключ должен быть списком! (list)")

        for item in key:
            if not isinstance(item, list) or len(item) != 2:
                raise err.KeyFormatError("Каждый элемент ключа должен быть списком [old, new]!")
            
            old, new = item
            text = text.replace(str(old), str(new))
    except Exception as e:
        raise err.KeyFormatError(f"Битый / неверный ключ! Ошибка: {e}") from None

    return text


def keys() -> dict:
    """
    просто функция которая возвращает разные ключи
    """
    dict_keys = {
        "Ru.Ru > En.Us": [
            ["А", "A"], ["В", "B"], ["Е", "E"], ["К", "K"], 
            ["М", "M"], ["Н", "H"], ["О", "O"], ["Р", "P"], 
            ["С", "C"], ["Т", "T"], ["Х", "X"], ["а", "a"], 
            ["е", "e"], ["о", "o"], ["р", "p"], ["с", "c"], 
            ["у", "y"], ["х", "x"]
        ],
        "En.Us > Ru.Ru": [
            ["A", "А"], ["B", "В"], ["E", "Е"], ["K", "К"], 
            ["M", "М"], ["H", "Н"], ["O", "О"], ["P", "Р"], 
            ["C", "С"], ["T", "Т"], ["X", "Х"], ["a", "а"], 
            ["e", "е"], ["o", "о"], ["p", "р"], ["c", "с"], 
            ["y", "у"], ["x", "х"]
        ]
    }
    return dict_keys