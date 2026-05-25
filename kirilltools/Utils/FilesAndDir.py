from pathlib import Path
import kirilltools.errors.FilesAndDir as _err
from os import remove as _rm
from shutil import rmtree as _rmtree

class GenStructures:
    """
    генерирует различные структуры папок и файлов
    """
    def __init__(self) -> None: 
        pass
    def GenProgectC(self, path) -> None:
        """
        создает структуру для С/С++ проекта
        """
        target_path = Path(path)
        if target_path.is_file():
            raise _err.IsFileError("путь указывает на файл")
        elif not target_path.is_dir():
            raise _err.NotPathError("такого пути не существует")
        else:
            dirs = ["bin", "build", "include", "lib", "src"]
            files = ["Makefile", "README.md"]
            two_level_files = [["include", "main.h"], ["src", "main.c"]]

            for dir_ in dirs:
                (target_path / dir_).mkdir(exist_ok=True)
            
            for file in files:
                (target_path / file).touch()
            
            for pathlist in two_level_files:
                (target_path / pathlist[0] / pathlist[1]).touch()

    def GenPyLib(self, path) -> None:
        """
        создает структуру для библиотеки python
        """
        target_path = Path(path)
        if target_path.is_file():
            raise _err.IsFileError("путь указывает на файл")
        elif not target_path.is_dir():
            raise _err.NotPathError("такого пути не существует")
        else:
            dirlib = "Lib"
            files = ["README.md", "setup.py", "pyproject.toml"]
            
            (target_path / dirlib).mkdir(exist_ok=True)
            
            with open(target_path / dirlib / "__init__.py", "w", encoding="utf-8") as init, \
                open(target_path / files[2], "w", encoding="utf-8") as pyprogct, \
                open(target_path / files[1], "w", encoding='utf-8') as setup, \
                open(target_path / files[0], "w", encoding="utf-8") as readme:
                
                setup.write("\nfrom setuptools import setup, find_packages\n\nsetup(\n    name='Lib',\n    version='0.0.1',\n    packages=find_packages()\n)\n")
                init.write("from . import *")
                pyprogct.write("\n[build-system]\nrequires = [\"setuptools>=61.0\", \"wheel\"]\nbuild-backend = \"setuptools.build_meta\"\n\n[project]\nname = \"Lib\"\nversion = \"0.0.1\"\nreadme = \"README.md\"\nrequires-python = \">=3.8\"\n\n[tool.setuptools]\npackages = [\"Lib\"]\n")

    def GenPyProgect(self, path) -> None:
        """
        создает структуру для проекта python
        """
        target_path = Path(path)
        if target_path.is_file():
            raise _err.IsFileError("путь указывает на файл")
        elif not target_path.is_dir():
            raise _err.NotPathError("такого пути не существует")
        else:
            dirs = ["Code", "Settings", "Bin"]
            files = ["README.md"]
            two_level_files = [["Settings", "main.json"], ["Code", "main.py"]]
            
            for dir_ in dirs:
                (target_path / dir_).mkdir(exist_ok=True)
            for file in files:
                (target_path / file).touch()
            for listing in two_level_files:
                (target_path / listing[0] / listing[1]).touch()

    def GenWeb(self, path) -> None:
        """
        генерирует структуру для html-сайта
        """
        target_path = Path(path)
        if target_path.is_file():
            raise _err.IsFileError("путь указывает на файл")
        elif not target_path.is_dir():
            raise _err.NotPathError("такого пути не существует")
        else:
            dirs = ["Styles", "Scripts"]
            files = ["README.md", "index.html"]
            two_level_files = [["Styles", "index.css"], ["Scripts", "index.js"]]
            
            for dir_ in dirs:
                (target_path / dir_).mkdir(exist_ok=True)
            for file in files:
                (target_path / file).touch()
            for listing in two_level_files:
                (target_path / listing[0] / listing[1]).touch()

def SortFiles(path) -> None:
    target_path = Path(path)
    if target_path.is_file():
        raise _err.IsFileError("путь указывает на файл")
    elif not target_path.is_dir():
        raise _err.NotPathError("такого пути не существует")
    else:
        images_dir = target_path / "Изображения"
        txt_dir = target_path / "Текст"
        pycode_dir = target_path / "Python код"
        pycache_dir = target_path / "Python кеш"
        c_dir = target_path / "C-C++ код"
        
        # Исправлено: добавили "C-C++ код" в список игнора
        service_dirs = ["Изображения", "Текст", "Python код", "Python кеш", "C-C++ код"]
        
        images_dir.mkdir(exist_ok=True)
        txt_dir.mkdir(exist_ok=True)
        pycode_dir.mkdir(exist_ok=True)
        pycache_dir.mkdir(exist_ok=True)
        c_dir.mkdir(exist_ok=True)

        pycache_count = 1
        
        for i in list(target_path.iterdir()):
            if i.is_file():
                ext = i.suffix.lower()
                if ext in ['.txt', '.md']:
                    i.rename(txt_dir / i.name)
                elif ext in ['.png', '.jpg', 'jpeg', '.webp']:
                    i.rename(images_dir / i.name)
                elif ext in [".py", ".pyi"]:
                    i.rename(pycode_dir / i.name)
                elif i.match("*.pyc"):
                    i.rename(pycache_dir / i.name)
                elif ext in [".c", ".cpp"]:
                    i.rename(c_dir / i.name)
            elif i.is_dir():
                if i.name in service_dirs:
                    continue
                    
                if i.name == "__pycache__":
                    i.rename(pycache_dir / f'{i.name}-{pycache_count}')
                    pycache_count += 1

def NoPycache(path):
    target_path = Path(path)
    if target_path.is_file():
        raise _err.IsFileError("путь указывает на файл")
    elif not target_path.is_dir():
        raise _err.NotPathError("такого пути не существует")
    else:
        for obj in target_path.rglob("*.pyc"):
            if obj.is_file():
                _rm(obj)
        for obj in target_path.rglob("__pycache__"):
            if obj.is_dir():
                _rmtree(obj)


__all__ = [
    "GenStructures", "SortFiles", "NoPycache"
]