import httpx, json, asyncio

class Get:
    def __init__(self, async_: bool = False):
        self.async_ = async_
        if self.async_:
            self.__client = httpx.AsyncClient(http1=True, follow_redirects=True)
        else:
            self.__client = httpx.Client(http1=True, follow_redirects=True)

    def _process_resp(self, resp):
        resjson = {
            "status code": resp.status_code,
            "http-vers": resp.http_version,
            "heds": dict(resp.headers),
            "cookie": dict(resp.cookies),
            "data": {"body": resp.text}
        }
        try:
            json1 = resp.json()
        except (json.JSONDecodeError, Exception):
            json1 = 'Not Json'
        resjson["data"]["json"] = json1
        return resjson, resp

    async def _async_get(self, url: str):
        try:
            resp = await self.__client.get(url)
            return self._process_resp(resp)
        except (httpx.ReadTimeout, httpx.ConnectError, httpx.ConnectTimeout):
            raise Exception('Нету подключения к интернету!')

    def _sync_get(self, url: str):
        try:
            resp = self.__client.get(url)
            return self._process_resp(resp)
        except (httpx.ReadTimeout, httpx.ConnectError, httpx.ConnectTimeout):
            raise Exception('Нету подключения к интернету!')

    def get(self, url: str):
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        if self.async_:
            return self._async_get(url)
        return self._sync_get(url)

    async def testinet(self):
        websites = ['http://google.com', 'http://pypi.org']
        if self.async_:
            tasks = [self.get(url) for url in websites]
            return list(await asyncio.gather(*tasks))
        else:
            return [self.get(url) for url in websites]

def ping():
    targets = {
        "google": "http://google.com",
        "dns гугла": "http://8.8.8.8",
        "dns cloudflare": "http://1.1.1.1",
        "yandex": "http://yandex.ru"
    }
    results = {}
    with httpx.Client(timeout=2.0) as http:
        for name, url in targets.items():
            try:
                http.get(url)
                results[name] = True
            except httpx.RequestError:
                results[name] = False
    
    return "\n".join([f"{k} ответил? {v}" for k, v in results.items()])