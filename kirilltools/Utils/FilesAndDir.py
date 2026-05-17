import kirilltools.errors.FilesAndDir as err
import os as _os

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
        if _os.path.isdir(path):
            pth = _os.getcwd()
            _os.chdir(path)
            dirs = ["bin", "build", "include", "lib", "src"]
            files = ["Makefile", "README.md"]
            two_level_files = [["include", "main.h"], ["src", "main.c"]]

            for dir_ in dirs:
                if not _os.path.exists(dir_):
                    _os.mkdir(dir_)
            
            for file in files:
                with open(file, "w", encoding="utf-8") as f:
                    pass
            
            for pathlist in two_level_files:
                full_file_path = _os.path.join(*pathlist) 
                with open(full_file_path, "w", encoding="utf-8") as f:
                    pass
            _os.chdir(pth)
        elif _os.path.isfile(path):
            raise err.IsFileError("путь указывает на файл") from None
        else:
            raise err.NotPathError("такого пути не существует") from None
    def GenPyLib(self, path) -> None:
        """
        создает структуру для библиотеки python
        """
        if _os.path.isdir(path):
            pth = _os.getcwd()
            _os.chdir(path)
            dirlib = "Lib"
            files = ["README.md", "setup.py", "pyproject.toml"]
            
            if not _os.path.exists(dirlib):
                _os.mkdir(dirlib)
            
            with open(_os.path.join(dirlib, "__init__.py"), "w", encoding="utf-8") as init, \
                open(files[2], "w", encoding="utf-8") as pyprogct, \
                open(files[1], "w", encoding='utf-8') as setup, \
                open(files[0], "w", encoding="utf-8") as readme:
                
                setup.write("\nfrom setuptools import setup, find_packages\n\nsetup(\n    name='Lib',\n    version='0.0.1',\n    packages=find_packages()\n)\n")
                init.write("from . import *")
                pyprogct.write("\n[build-system]\nrequires = [\"setuptools>=61.0\", \"wheel\"]\nbuild-backend = \"setuptools.build_meta\"\n\n[project]\nname = \"Lib\"\nversion = \"0.0.1\"\nreadme = \"README.md\"\nrequires-python = \">=3.8\"\n\n[tool.setuptools]\npackages = [\"Lib\"]\n")
            _os.chdir(pth)
        elif _os.path.isfile(path):
            raise err.IsFileError("путь указывает на файл") from None
        else:
            raise err.NotPathError("такого пути не существует") from None
    def GenPyProgect(self, path) -> None:
        """
        создает структуру для проекта python
        """
        if _os.path.isdir(path):
            pth = _os.getcwd()
            _os.chdir(path)
            dirs = ["Code", "Settings", "Bin"]
            files = ["README.md"]
            two_level_files = [["Settings", "main.json"], ["Code", "main.py"]]
            for dir_ in dirs:
                if not _os.path.exists(dir_):
                    _os.mkdir(dir_)
            for file in files:
                with open(file, "w", encoding="utf-8"): pass
            for listing in two_level_files:
                with open(_os.path.join(*listing), "w", encoding="utf-8"): pass
            _os.chdir(pth)

        elif _os.path.isfile(path):
            raise err.IsFileError("путь указывает на файл") from None
        else:
            raise err.NotPathError("такого пути не существует") from None
    def GenWeb(self, path):
        """
        генерирует структуру для html-сайта
        """
        if _os.path.isdir(path):
            pth = _os.getcwd()
            _os.chdir(path)
            dirs = ["Styles", "Scripts"]
            files = ["README.md", "index.html"]
            two_level_files = [["Styles", "index.css"], ["Scripts", "index.js"]]
            for dir_ in dirs:
                if not _os.path.exists(dir_):
                    _os.mkdir(dir_)
            for file in files:
                with open(file, "w", encoding="utf-8"): pass
            for listing in two_level_files:
                with open(_os.path.join(*listing), "w", encoding="utf-8"): pass
            _os.chdir(pth)
        elif _os.path.isfile(path):
            raise err.IsFileError("путь указывает на файл") from None
        else:
            raise err.NotPathError("такого пути не существует") from None