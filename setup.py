from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.3.0-alpha5',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil', # psutil
        "rich", "markdown-it-py", "pygments" # rich и зависимости
    ],
    license="GPL-3.0-or-later",
    description=
    """
1. убрана лишняя строчка цвета в kirilltools.taskmgr (удаление)
2. удалены комментарии (код можно и самому изучить а вот место занимает) (удаление)
3. добавление дополнительных инструментов (директория /kirilltools/utils) (добавление)
4. добавлены дополнительные ошибки для модуля kirilltools.Utils.iter (добавление)
5. добавлена функция декодирования шифра цезаря (добавление)
6. исправлена аннотация типов в модуле шифров (было указано что возвращает dict но на самом деле: str) (исправление)
    """
)
