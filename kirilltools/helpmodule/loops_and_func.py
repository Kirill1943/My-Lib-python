import kirilltools.helpmodule.basefunc as _help
import time as _time
from kirilltools.errors.base import ForceInterruptionError as _ForceInterruptionError

def help1(): _help.help1() 
def help2(): _help.help2()
def help3(): _help.help3()

def help4() -> None:
    txt = '''
так-же в пайтоне имеются циклы! это такие штуки которые позволяют выполнять действия несколько раз
начнем с while: это простой цикл который выполняется пока условие верно:

a = 10 # делаем счетчик

while a > 1:
    a -= 1
    print('цикл сделан!')

еще есть такое понятие как бесконечный цикл - но если что его не рекомендуется делать:

while True: # while это как пока а True это верно. пока верно. или пока верно равно верно, цикл замкнут
    pass 

и имеется for - это цикл-счетчик, мы пишем for, затем переменную счетчика например i, затем in, и то что нужно перебрать:

for i in range(1, 6): # range(a, b) это как числа от числа a до числа перед b тоесть b-1
    print(i)
вот что выведет:
1
2
3
4
5
мы создали простейший счетчик от 1 до 5!
'''
    try:
        for i in txt:
            print(i, end='', flush=True)
            _time.sleep(0.001)
    except KeyboardInterrupt:
        raise _ForceInterruptionError("ты прервал скрипт") from None

def help5() -> None:
    txt = '''
а теперь разберем функции. представь - у тебя есть какой-то кусок кода
который постоянно нужен. ты постоянно его пишешь и пишешь, ПРЕКРАЩАЙ ТАК ДЕЛАТЬ!
за тебя уже все продумали. в пайтоне есть функции! они обьявляются с помощью ключевого
слова def:

# def # ключевое слово
# def myfunc # название
# def myfunc() -> None: # скобки и двоеточие
# def myfunc() -> None: 
#   pass # а вот это уже функция!

именно так они и создаются! а в скобках указываются аргументы, например:

def func(a, b):
    print(a + b)

выведет сумму введенных чисел! но только если это числа
в пайтоне так-же имеется return - это случай для функций. он заставляет функцию возвращать значение
например ввел ты название функции и скобки. например func() -> None, без return тут появится None - ничего
а если функция что-то вернет. то это значение будет как-бы заменено:

def add(a, b):
    return a + b

print(add(5, 5)) # выведет 10

вот! на месте add(5, 5) появилось 10. в итоге вышло простое print(10)!
а еще в пайтоне имееются звездочки для аргументов. смотри: *args берет все простые значения в список
а **kwargs! он собирает именованные значения в словарь. типа {"name": 123}..

def add_all(*args):
    summa = 0
    for i in args:
        summa += float(i)
    return summa

а теперь разберем декораторы. - представь, у тебя есть какая-то функция. но ты хочешь добавить новый
функционал НЕ изменяя функцию, для этого служат декораторы, они пишутся через @ и это такие же функции:

def decorate(func): # декоратор будет принимать функцию
    def runner(*a, **k): # это уже сам можно сказать механизм, принимает любые аргументы
        return f"вернуло: {func(*a, **k)}" # передаем аргументы внутрь func!
    return runner # возвращаем двигатель

@decorate # И ТЕПЕРЬ УЖЕ используем декоратор
def add(a, b):
    return a + b

обьясняю как эта штуковина работает: пайтон просто подменяет твою функцию вот так:

add = decorate(add)

А DECORATE ПРИНИМАЕТ ФУНКЦИЮ! и возвращает двигатель. в итоге выходит что функцию мы заменили или ДОПОЛНИЛИ!
'''
    try:
        for i in txt:
            print(i, end='', flush=True)
            _time.sleep(0.001)
    except KeyboardInterrupt:
        raise _ForceInterruptionError("ты прервал скрипт") from None

def help6() -> None:
    txt = ''''''
    try:
        for i in txt:
            print(i, end='', flush=True)
            _time.sleep(0.001)
    except KeyboardInterrupt:
        raise _ForceInterruptionError("ты прервал скрипт") from None

__all__ = [
    "help1", "help2",
    "help3", "help4",
    "help5", "help6"
]