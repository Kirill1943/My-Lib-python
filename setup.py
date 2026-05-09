from setuptools import setup, find_packages

setup(
    name='Kirilltools',
    version='0.3.0-alpha9',
    packages=find_packages(),
    install_requires=[
        'httpx', 'h11', 'httpcore', 'anyio', # httpx и зависимости
        'psutil', # psutil
        "rich", "markdown-it-py", "pygments" # rich и зависимости
    ],
    license="GPL-3.0-or-later",
    description='6 добавлений 2 удаления',
    author="kirill1943",
    url="https://github.com/Kirill1943/My-Lib-python",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown'
)
