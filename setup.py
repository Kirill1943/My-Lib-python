from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.3.0-alpha2',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil' # psutil
    ],
    description="были добавлены 2 вида ключа в файл chiper.py и прокачан справочный модуль"
)
