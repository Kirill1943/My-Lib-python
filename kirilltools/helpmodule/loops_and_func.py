import basefunc
import time
from kirilltools.errors.base import ForceInterruptionError

def help1(): basefunc.help1()
def help2(): basefunc.help2()
def help3(): basefunc.help3()

def help4():
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
            time.sleep(0.001)
    except KeyboardInterrupt:
        raise ForceInterruptionError("ты прервал скрипт") from None



