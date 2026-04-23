from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.2.5',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil' # psutil
    ],
    description="улучшен справочный модуль и немного улучшен taskmgr"
)
