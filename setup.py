from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.3.0-alpha6',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil', # psutil
        "rich", "markdown-it-py", "pygments" # rich и зависимости
    ],
    license="GPL-3.0-or-later",
    description=
    """
1. добавлены декораторы в модуль utils (добавление)
2. добавлены ошибки для декораторов в модуль errors (добавление)
    """
)
