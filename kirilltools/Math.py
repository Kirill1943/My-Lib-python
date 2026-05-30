import kirilltools.errors.math as err
import kirilltools.errors.base as baseerr

def get_kilo(square_meters: float, kilo_in_one_meter_cubed: float = 1) -> float:
    try:
        square_meters = float(square_meters)
        kilo_in_one_meter_cubed = float(kilo_in_one_meter_cubed)
    except (ValueError, TypeError):
        raise err.TypesError("нельзя умножить строки и числа и получить массу!") from None
    except KeyboardInterrupt:
        raise baseerr.ForceInterruptionError("скрипт прерван")
    kg = kilo_in_one_meter_cubed * square_meters
    return float(kg)

def tetration(num: int, height: int) -> int:
    """
    Математическая операция тетрации (башня степеней)
    height - сколько раз число возводится в свою степень
    """
    try:
        num, height = int(num), int(height)
    except (ValueError, TypeError):
        raise err.TypesError("ты ввел не число в один из аргументов")
    try:
        if height == 0: return 1
        result = num
        for _ in range(height - 1):
            result = num ** result
        return result
    except OverflowError:
        raise err.NumOwerflowError("слишком огромное число") from None
    except MemoryError:
        raise baseerr.MemoryEndError("память переполнилась")
    except KeyboardInterrupt:
        raise baseerr.ForceInterruptionError("скрипт прерван")

def double_factorial(x: int) -> int:
    """
    двойной факториал который умножает числа n 
    только той же разрядности что и n
    
    например: 5!! = 1 * 3 * 5 = 15
    """
    try:
        x = int(x)
    except (ValueError, TypeError):
        raise err.TypesError("ты ввел не число!")
    except KeyboardInterrupt:
        raise baseerr.ForceInterruptionError("скрипт прерван")
    if x <= 0:
        return 1
    result = 1
    for i in range(x, 0, -2):
        result *= i
    return result

def fib(x: int, print_result=False) -> list:
    """
    вычисляет числа фибоначчи, а именно 
    числа с суммой 2 прошлых чисел

    x: количество чисел фибоначчи
    """
    try:
        x = int(x)
    except (ValueError, TypeError):
        raise err.TypesError("ты ввел не число!")
    if x < 0:
        raise err.TypesError("x должен быть не меньше 0!")
    elif x == 0:
        return []
    try:
        result = []
        a, b = 0, 1
        c = a + b
        result.append(c)
        while c < x:
            a, b = b, a + b
            c = a + b
            if print_result: print(c, end=' ')
            result.append(c)
    except KeyboardInterrupt:
        raise baseerr.ForceInterruptionError("скрипт прерван")
    return result

__all__ = [
    "tetration", "double_factorial", 
    "get_kilo", "fib"
]