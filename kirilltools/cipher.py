from kirilltools.errors.math import TypesError
import kirilltools.errors.cipherError as err

def Caesar_cipher(text: str, next: int = 1024) -> str:
    """
    распостраненный шифр цезаря который сдвигает 
    каждую букву на несколько позиций вперед в unicode
    """
    try:
        next = int(next)
    except (ValueError, TypeError):
        raise TypesError("ты ввел не число в поле next!") from None
    
    return_text = ''
    for i in text:
        # ФИКС ТУТ: считаем остаток от суммы, чтобы не вылетало за 0x110000
        i = chr((ord(i) + next) % 1114112)
        return_text = return_text + str(i)
    return return_text

def Super_Caesar_Cipher(text: str, next: int = 1024, once: int = 2):
    """
    кодирует шифром цезаря несколько раз подряд
    """
    try:
        once = int(once)
    except (ValueError, TypeError):
        raise TypesError("ты ввел не число в поле once!") from None
    result = text
    for i in range(once):
        result = Caesar_cipher(result, next=next)
    return result

def Super_Uncode_Caesar_Cipher(text: str, next: int = 1024, once: int = 2):
    """
    декодирует шифр цезаря несколько раз подряд
    """
    try:
        once = int(once)
    except (ValueError, TypeError):
        raise TypesError("ты ввел не число в поле once!") from None
    result = text
    for i in range(once):
        result = uncoding_caesar_cipher(result, next=next)
    return result

def uncoding_caesar_cipher(text: str, next: int = 1024):
    """
    декодирует шифр цезаря сдвигая
    каждую букву текста на позиции назад
    """
    try:
        next = int(next)
    except (ValueError, TypeError):
        raise TypesError("ты ввел не число в поле next!") from None
    
    return_text = ''
    for i in text:
        # ФИКС ТУТ: считаем остаток от разности, чтобы не уходило в минус
        i = chr((ord(i) - next) % 1114112)
        return_text = return_text + str(i)
    return return_text

def custom_cipher(text: str, key: list) -> str:
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
