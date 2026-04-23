from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.2.4',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil' # psutil
    ]
)
