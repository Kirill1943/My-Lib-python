import httpx, json, asyncio
import kirilltools.errors.base as err
class Get:
    def __init__(self, async_: bool = False):
        self.async_ = async_
        if self.async_:
            self.__client = httpx.AsyncClient(http1=True, follow_redirects=True)
        else:
            self.__client = httpx.Client(http1=True, follow_redirects=True)
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__client.aclose()
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
            resp.aclose()
            return self._process_resp(resp)
        except (httpx.ReadTimeout, httpx.ConnectError, httpx.ConnectTimeout):
            raise Exception('Нету подключения к интернету!')

    def _sync_get(self, url: str):
        try:
            resp = self.__client.get(url)
            resp.close()
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

def MultCheck(http1=True, http2=True, log=False):
    result = ""
    try:
        with httpx.Client(http1=http1, http2=http2, follow_redirects=True, timeout=3) as client:
            try:
                github = client.get('http://github.com').status_code
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.ConnectTimeout, httpx.TimeoutException, httpx.RequestError):
                github = 0
            if log:
                print(f"github: {"Ответил" if github != 0 else "Нет соединения"}, status code: {github}")
            result += f"github: {"Ответил" if github != 0 else "Нет соединения"}, status code: {github}"
            try:
                yandex = client.get("http://yandex.ru").status_code
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.ConnectTimeout, httpx.TimeoutException, httpx.RequestError):
                yandex = 0
            if log:
                print(f"yandex: {"Ответил" if yandex != 0 else "Нет соединения"}, status code: {yandex}")
            result += f'\nyandex: {"Ответил" if yandex != 0 else "Нет соединения"}, status code: {yandex}'
            try:
                google = client.get("http://google.com").status_code
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.ConnectTimeout, httpx.TimeoutException, httpx.RequestError):
                google = 0
            if log:
                print(f"google: {"Ответил" if google != 0 else "Нет соединения"}, status code: {google}")
            result += f"\ngoogle: {"Ответил" if google != 0 else "Нет соединения"}, status code: {google}"
            try:
                googledns = client.get("http://8.8.8.8").status_code
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.ConnectTimeout, httpx.TimeoutException, httpx.RequestError):
                googledns = 0
            if log:
                print(f"dns google: {"Ответил" if googledns != 0 else "Нет соединения"}, status code: {googledns}")
            result += f"\ndns google: {"Ответил" if googledns != 0 else "Нет соединения"}, status code: {googledns}"
            try:
                pypi = client.get("http://pypi.org").status_code
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.ConnectTimeout, httpx.TimeoutException, httpx.RequestError):
                pypi = 0
            if log:
                print(f"pypi: {"Ответил" if pypi != 0 else "Нет соединения"}, status code: {pypi}")
            result += f"\npypi: {"Ответил" if pypi != 0 else "Нет соединения"}, status code: {pypi}"
                
    except KeyboardInterrupt:
        raise err.ForceInterruptionError("скрипт прерван") from None
    return result