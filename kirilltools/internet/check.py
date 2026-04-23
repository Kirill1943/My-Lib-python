import httpx, json, asyncio
from kirilltools.errors.Wifi import ConnectError, HttpsError

class Get:
    def __init__(self, async_: bool = False):
        self.async_ = async_
        if self.async_:
            self.__client = httpx.AsyncClient(http1=True, follow_redirects=True)
        else:
            self.__client = httpx.Client(http1=True, follow_redirects=True)

    async def get(self, url: str):
        """
        1 элемент списка - результат get-инга
        2 элемент списка - переменная get-а
        """
        if url.startswith('https://'):
            raise HttpsError('Библиотека не поддерживает https')
        if not url.startswith('http://'):
            url = 'http://' + url
        try:
            if self.async_:
                resp = await self.__client.get(url)
            else:
                resp = self.__client.get(url)
        except (httpx.ReadTimeout, httpx.ConnectError, httpx.ConnectTimeout):
            raise ConnectError('Нету подключения к интернету!')
        else:
            resjson = {
                "status code": resp.status_code,
                "http-vers": resp.http_version,
                "heds": dict(resp.headers),
                "cookie": dict(resp.cookies),
                "data": {
                    "body": resp.text
                }
            }
            try:
                json1 = resp.json()
            except json.JSONDecodeError:
                json1 = 'Not Json'
            resjson["data"]["json"] = json1
            return resjson, resp
    async def testinet(self):
        websites = ['http://google.com', 'http://pypi.org']
        try:
            if self.async_:
                tasks = [self.get(url) for url in websites]
                # Собираем всё в один список
                a = list(await asyncio.gather(*tasks))
            else:
                a = []
                for i in websites:
                    res = await self.get(i)
                    a.append(res)
            return a
        except (httpx.ReadTimeout, httpx.ConnectError, httpx.ConnectTimeout):
            raise ConnectError('нету соединения')
