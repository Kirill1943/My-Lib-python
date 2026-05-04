from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.3.0-alpha3',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil' # psutil
    ],
    description=
    """
1. исправлена проблема в модуле kirilltools.Math: при вводе не числа не обрабатывалась ошибка ValueError ведь код был рассчитан на TypeError (решение: добавление проверки исключения ValueError)
2. такая же ошибка как и 1 но уже в модуле kirilltools.cipher (решение: такое же как и в 1)
3. модуль kirilltools.helpmodule.loops_and_func не находил basefunc (решение: basefunc заменен на полный путь: kirilltools.helpmodule.basefunc)
4. как всегда расширил справочник
    """
)
