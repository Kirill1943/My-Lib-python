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
        i = chr((ord(i) + next) % 1114112)
        return_text = return_text + str(i)
    return return_text

def Super_Caesar_Cipher(text: str, next: int = 1024, once: int = 2) -> str:
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

def Super_Uncode_Caesar_Cipher(text: str, next: int = 1024, once: int = 2) -> str:
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

def uncoding_caesar_cipher(text: str, next: int = 1024) -> str:
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
        i = chr((ord(i) - next) % 1114112)
        return_text = return_text + str(i)
    return return_text

def custom_cipher(text: str, key: list) -> str:
    """
    Шифрует сообщение пользовательским ключом за один безопасный проход,
    чтобы символы не перезаписывали друг друга по цепочке.
    """
    if not isinstance(key, list):
        raise err.KeyFormatError("Ключ должен быть списком! (list)")
    for item in key:
        if not isinstance(item, list) or len(item) != 2:
            raise err.KeyFormatError("Каждый элемент ключа должен быть списком [old, new]!")

    try:
        translation_table = {ord(str(old)[0]): str(new) for old, new in key}
        return text.translate(translation_table)
    except Exception as e:
        raise err.KeyFormatError(f"Битый / неверный ключ! Ошибка: {e}") from None


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
