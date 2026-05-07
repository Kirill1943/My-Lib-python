import kirilltools.errors.math as err

class MathTasks:
    """
    в этом классе описаны простые математические задания
    """
    def __init__(self):
        pass
    def task1(self, a, b, c):
        """
        задача: вычисление суммы a и b умноженной на c: (a + b) * c
        """
        try:
            a, b, c = float(a), float(b), float(c)
        except (ValueError, TypeError):
            raise err.TypesError("одна или больше из входных значений это строка / bool!")
        return (a + b) * c
    def task2(self, a, b, c):
        """
        задача: было a единиц. вычли произведение b и c
        формула: a - (b * c)
        """
        try:
            a, b, c = float(a), float(b), float(c)
        except (ValueError, TypeError):
            raise err.TypesError("одна или больше из входных значений это строка / bool!")
        return a - (b * c)
def get_kilo(square_meters, kilo_in_one_meter_cubed=1) -> float:
    try:
        square_meters = float(square_meters)
        kilo_in_one_meter_cubed = float(kilo_in_one_meter_cubed)
    except (ValueError, TypeError):
        raise err.TypesError("нельзя умножить строки и числа и получить массу!") from None
    kg = kilo_in_one_meter_cubed * square_meters
    return float(kg)

def tetration(num, height):
    """
    Математическая операция тетрации (башня степеней)
    height - сколько раз число возводится в свою степень
    """
    try:
        if height == 0: return 1
        result = num
        for _ in range(height - 1):
            result = num ** result
        return result
    except OverflowError:
        raise err.NumOwerflowError("слишком огромное число")