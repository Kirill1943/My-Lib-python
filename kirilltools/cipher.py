from kirilltools.errors.math import TypesError
import kirilltools.errors.cipherError as err
from typing import overload

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
        next = int(next)
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
        next = int(next)
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

@overload
def Vigenere_cipher(text: str, key: list[int]) -> str: ...

@overload
def Vigenere_cipher(text: str, key: str) -> str: ...

def Vigenere_cipher(text: str, key: list[int] | str) -> str:
    """
    Шифрует шифром Виженера по кодам Юникода.
    Каждый символ сдвигается на число из списка key по нужному индексу
    """
    if not key:
        return text
    
    # Если пришла строка, превращаем каждый символ в его Юникод-код
    if isinstance(key, str):
        working_key = [ord(k) for k in key]
    else:
        working_key = key
        
    result = ''
    key_length = len(working_key)
    
    for i, char in enumerate(text):
        current_shift = working_key[i % key_length]
        new_unicode = ord(char) + current_shift
        result = result + chr(new_unicode)
    return result

@overload
def Uncode_Vigenere_cipher(text: str, key: list[int]) -> str: ...

@overload
def Uncode_Vigenere_cipher(text: str, key: str) -> str: ...

def Uncode_Vigenere_cipher(text: str, key: list[int] | str) -> str:
    """
    раскодировывает шифром Виженера по кодам Юникода.
    Каждый символ сдвигается назад на число из списка key по нужному индексу
    """
    if not key:
        return text

    if isinstance(key, str):
        working_key = list(map(ord, key))
    else:
        working_key = key
        
    result = ''
    key_length = len(working_key)
    
    for i, char in enumerate(text):
        current_shift = working_key[i % key_length]
        new_unicode = ord(char) - current_shift
        result = result + chr(new_unicode)
    return result

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


__all__ = [
    "keys", "custom_cipher",
    "uncoding_caesar_cipher",
    "Super_Uncode_Caesar_Cipher",
    "Super_Caesar_Cipher", "Caesar_cipher",
    "Uncode_Vigenere_cipher", "Vigenere_cipher"
]