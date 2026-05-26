1. добавлен асинхронный метод в kirilltools.internet.check AsyncMultCheck (добавление)
2. мелкое исправление kirilltools.Utils.FilesAndDir.SortFiles, забыл поставить точку перед jpeg (line 130: elif ext in ['.png', '.jpg', '.jpeg', '.webp']:) (мелкое исправление)
3. добавлен +1 новый ресурс для kirilltools.internet.check.MultCheck, kirilltools.internet.check.AsyncMultCheck (добавление)
4. список ресурсов переставлен в глобальную видимость и превращен в константу (переставление + переиминовывание)
5. добавлена защита в kirilltools.internet.check.Get от вызова не того метода GET-а (добавление защиты)
6. исправлены ip-адреса в списке целей kirilltools.internet.check.ping (исправление)

итог: 3 добавления (2 обычных, 1 безопасности) 2 исправления 1 перенос 1 переименование