from time import time as unixtime, sleep
from rich import print
from functools import wraps
from secrets import token_urlsafe as gentoken
from rich.live import Live
import kirilltools.errors.decorators as err
import threading

def time_meter(func):
    """
    замеряет время выполнения функции
    """
    @wraps(func)
    def runner(*a, **k):
        start = unixtime()
        result = func(*a, **k)
        end = unixtime()
        print(f'[#00FF00] функция сработала за {end - start:.9f} секунд')
        return result
    return runner
def keylocker(password=gentoken(8), getpassword=False):
    """
    блокирует выполнение функции если не ввел пароль
    если не успел ввести в течении 45 секунд то вылетает исключение
    """
    def decorate(func):
        @wraps(func)
        def runner(*a, **k):
            print(f'[#FF0000]Инициализация защиты... (Пароль: {'#'*8 if not getpassword else password})')
            
            remaining_time = 40
            unlocking = False
            user_input = ""

            def get_input():
                nonlocal user_input, unlocking
                user_input = input("\nВведите пароль: ")
                if user_input == password:
                    unlocking = True

            input_thread = threading.Thread(target=get_input, daemon=True)
            input_thread.start()
            try:
                with Live("", refresh_per_second=10) as live:
                    while remaining_time > 0 and not unlocking:
                        color = '#FF0000' if remaining_time < 15 else '#FFFF00'
                        live.update(f'[{color}]Осталось: {remaining_time} сек. ВВОДИ ПАРОЛЬ!')
                        
                        sleep(1)
                        remaining_time -= 1
            except KeyboardInterrupt:
                pass
            
            if unlocking:
                print("[#00FF00]ДОСТУП РАЗРЕШЕН!")
                return func(*a, **k)
            else:
                raise err.NotUnlockError("Время вышло! Ты не успел!") from None
        return runner
    return decorate

def nerd(func):
    @wraps(func)
    def runner(*a, **k):
        try:
            def test():
                print('nerd: КТО УМНЕЕ: Я ИЛИ ТЫ?')
                if input("Ответ: ") != "ты":
                    print('[#FF0000]NERD: НЕВЕРНО! ПШЕЛ ИЗ МОЕЙ ШКОЛЫ!')
                    raise err.TrubkaError("nerd обозвал тебя тупицей") from None
                print('nerd: ВЕРНО!')
                return func(*a, **k)

            print('nerd: ТААК! ХОЧЕШЬ ТУТ ФУНКЦИЮ ЗАПУСТИТЬ? ДАВАЙ ОТВЕЧАЙ')
            result = input("Да или Нет?: ")
            
            if result != "Да":
                print("nerd: ТЕБЯ НЕ СПРАШИВАЛИ БЫСТРО ОТВЕТЬ!")
            else:
                print('nerd: ТЕПЕРЬ ОТВЕЧАЙ:')
            
            return test()

        except KeyboardInterrupt:
            print("\n[#FF0000]nerd: КУДА ПОБЕЖАЛ?!")
            raise err.LogoutError("ты сбежал от этого психа но функция не выполнилась") from None
    return runner

@nerd
def a():
    pass
a()