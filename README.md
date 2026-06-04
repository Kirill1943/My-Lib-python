### моя библиотека
я - автор этого репозитория заинтересовался в том чтобы создать свою библиотеку python которую можно установить с помощью pip
### поддерживается:
✅ тесты [tests/ для тестирования проекта]
✅ шифрование цезаря (модуль kirilltools.cipher)
✅ современный способ установки с помощью pyproject.toml
✅ модуль гетинга (kirilltools.internet)
✅ справочный модуль (kirilltools.helpmodule)
✅ тетрация, двойной факториал в модуле kirilltools.Math
✅ собственный монитор ресурсов (kirilltools.taskmgr)
### примеры использования:
#### монитор ресурсов
```py
from kirilltools import taskmgr

monitor = taskmgr.monitor(fps=40)
monitor.run()
```
#### математические операции
```py
from kirilltools import Math

print(f'3 в тетрации 2: {Math.tetration(3, 2)}')
print(f'двойной факториал 4: {Math.double_factorial(4)}')
```
#### шифрование цезаря
```py
from kirilltools import cipher

text_for_uncode = cipher.Caesar_cipher("hello world", 16)
print(f'зашифрованное послание: {text_for_uncode}, расшифрованное: {cipher.uncoding_caesar_cipher(text_for_uncode, 16)}')
```
### зависимости

**rich** - цветные логи и цветное отображение текста а так-же Live
**httpx** - современный вариант для взаимодействия с API и сетью, нужно для модуля гетинга (kirilltools.internet)
**GPUtil** - нужно для отображения информации об видеокартах
**psutil** - узнавать информацию об системе для kirilltools.taskmgr
### кто помог проекту?
* [Giampaolo Rodola](https://github.com/giampaolo) - а конкретнее его библиотека python psutil, она помогла в модуле kirilltools.taskmgr, без его библиотеки я автор проекта не смог бы реализовать модуль
* [Tom Christie](https://github.com/tomchristie) - проекту помогла его библиотека python httpx, она помогла в модуле kirilltools.internet, без его проекта модуля бы просто не было
* [Will McGugan](https://github.com/willmcgugan) - создатель rich, именно с помощью его библиотеки я смог реализовать красоту отображения
### актуальные команды для скачивания:
```sh
# 1 способ (через исходный код)
git clone https://github.com/kirill1943/My-Lib-Python.git
cd "My-Lib-Python"
pip install .
# 2 способ (напрямую)
pip install git+https://github.com/kirill1943/My-Lib-Python
```

какой рекомендуется?: автор выбирает **1 способ** но для вас рекомендуется **2 способ**

|способ|плюсы|минусы|описание|
|:-:|:-:|:-:|:-:|
|через исходники|можно быстро посмотреть код|останется лишнее|для того чтобы модифицировать код или тестировать конкретные части без импорта всей либы|
|напрямую|сразу установится|придется лесть в site-packages чтобы смотреть код|если хочешь просто установить библиотеку - выбирай этот способ|
