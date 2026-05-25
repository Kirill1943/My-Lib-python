import httpx as _httpx
import json as _json
import asyncio as _asyncio
import kirilltools.errors.base as _err

class Get:
    def __init__(self, async_: bool = False) -> None:
        self.async_ = async_
        if self.async_:
            self.__client: _httpx.AsyncClient = _httpx.AsyncClient(http1=True, follow_redirects=True)
        else:
            self.__client: _httpx.Client = _httpx.Client(http1=True, follow_redirects=True)

    def __enter__(self) -> "Get":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__client.close()

    async def __aenter__(self) -> "Get":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.__client.aclose()

    def _process_resp(self, resp: _httpx.Response) -> list:
        res_json = {
            "status code": resp.status_code,
            "http-vers": resp.http_version,
            "heds": dict(resp.headers),
            "cookie": dict(resp.cookies),
            "data": {"body": resp.text}
        }
        try:
            _json1 = resp.json()
        except (_json.JSONDecodeError, Exception):
            _json1 = 'Not _json'
        res_json["data"]["_json"] = _json1
        return [res_json, resp]

    async def _async_get(self, url: str) -> dict:
        try:
            resp = await self.__client.get(url)
            return self._process_resp(resp)
        except (_httpx.ReadTimeout, _httpx.ConnectError, _httpx.ConnectTimeout):
            raise Exception('Нету подключения к интернету!')

    def _sync_get(self, url: str) -> dict:
        try:
            resp = self.__client.get(url)
            return self._process_resp(resp)
        except (_httpx.ReadTimeout, _httpx.ConnectError, _httpx.ConnectTimeout):
            raise Exception('Нету подключения к интернету!')

    async def aget(self, url: str) -> dict:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        return await self._async_get(url)

    def get(self, url: str) -> dict:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        if self.async_:
            raise RuntimeError("Для асинхронного режима используйте метод aget() с await!")
        return self._sync_get(url)

    async def testinet(self) -> list:
        websites = ['http://google.com', 'http://pypi.org']
        if self.async_:
            tasks = [self.aget(url) for url in websites]
            return list(await _asyncio.gather(*tasks))
        else:
            return [self.get(url) for url in websites]

def ping() -> str:
    targets = {
        "google": "http://google.com",
        "dns гугла": "http://8.8.8",
        "dns cloudflare": "http://1.1.1",
        "yandex": "http://yandex.ru"
    }
    results = {}
    with _httpx.Client(timeout=2.0) as http:
        for name, url in targets.items():
            try:
                http.get(url)
                results[name] = True
            except _httpx.RequestError:
                results[name] = False
    
    return "\n".join([f"{k} ответил? {v}" for k, v in results.items()])

def MultCheck(http1: bool = True, http2: bool = True, log: bool = False) -> str:
    try: 
        import h2
        http2 = True if http2 else False
    except ImportError: 
        http2 = False
    targets = [
        ("github", "http://github.com"),
        ("yandex", "http://yandex.ru"),
        ("google", "http://google.com"),
        ("dns google", "http://8.8.8.8"),
        ("pypi", "http://pypi.org")
    ]
    lines = []
    try:
        with _httpx.Client(http1=http1, http2=http2, follow_redirects=True, timeout=3) as client:
            for name, url in targets:
                try:
                    status = client.get(url).status_code
                except (_httpx.ConnectError, _httpx.ReadTimeout, _httpx.ConnectTimeout, _httpx.TimeoutException, _httpx.RequestError):
                    status = 0
                
                msg = f"{name}: {'Ответил' if status != 0 else 'Нет соединения'}, status code: {status}"
                if log:
                    print(msg)
                lines.append(msg)
                
    except KeyboardInterrupt:
        raise _err.ForceInterruptionError("скрипт прерван") from None
        
    return "\n".join(lines)

__all__ = [
    "MultCheck", "ping", "Get"
]