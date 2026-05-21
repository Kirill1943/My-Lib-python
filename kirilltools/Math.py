import kirilltools.errors.math as err
import kirilltools.errors.base as baseerr

def get_kilo(square_meters: float, kilo_in_one_meter_cubed: float = 1) -> float:
    try:
        square_meters = float(square_meters)
        kilo_in_one_meter_cubed = float(kilo_in_one_meter_cubed)
    except (ValueError, TypeError):
        raise err.TypesError("нельзя умножить строки и числа и получить массу!") from None
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

def double_factorial(x) -> int:
    try:
        x = int(x)
    except (ValueError, TypeError):
        raise err.TypesError("ты ввел не число!")
    if x <= 0:
        return 1
    result = 1
    for i in range(x, 0, -2):
        result *= i
    return result
