from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.3.0-alpha4',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil', # psutil
        "rich", "markdown-it-py", "pygments" # rich и зависимости
    ],
    license="GPL-3.0-or-later",
    description=
    """
1. немного улучшена справка (добавление)
2. доделан диспетчер задач (добавление)
3. убрана заметка в kirilltools.taskmgr (говорю как автор: дело в том что у меня vscode, а я использую подсветку редактора чтобы подбирать нормальный hex, и я забыл про эту заметку и она запушилась в репозиторий) (удаление)
4. убрана строчка monitor() в kirilltools.taskmgr (говорю снова как автор: сорян ребят я тестировал код и забыл про if __name__ == "__main__":) (удаление)
    """
)
