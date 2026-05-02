from kirilltools.errors.math import TypesError
import kirilltools.errors.cipherError as err

def Caesar_cipher(text: str, next: int = 1024):
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

def custom_cipher(text: str, key: list):
    """
    это функция позволяющая зашифровать своим ключом
    сообщение. работает это по принципу списков в списке, пример:
    text = abc
    key = [["a", "b"], ["c", "b"]]
    вернет bbb
    """
    try:
        # 1. Проверяем, что ключ - это список
        if not isinstance(key, list):
            raise err.KeyFormatError("Ключ должен быть списком! (list)")

        for item in key:
            # 2. Проверяем, что каждый элемент - тоже список из 2 элементов
            if not isinstance(item, list) or len(item) != 2:
                raise err.KeyFormatError("Каждый элемент ключа должен быть списком [old, new]!")
            
            old, new = item
            # 3. Сама замена
            text = text.replace(str(old), str(new))
    except Exception as e:
        # Если случилось что-то совсем странное
        raise err.KeyFormatError(f"Битый / неверный ключ! Ошибка: {e}") from None

    return text


