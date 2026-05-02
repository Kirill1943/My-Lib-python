from setuptools import setup, find_packages

setup(
    name='Kiriltools',
    version='0.3.0-alpha1',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil' # psutil
    ],
    description="были добавлены маленькие изменения math модуля и модуль шифрования"
)
