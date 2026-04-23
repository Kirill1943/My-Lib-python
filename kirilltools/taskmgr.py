import platform, psutil
import rich.live

class ramInfo:
    def __init__(self):
        pass
    def getram(self) -> dict:
        geter = psutil.virtual_memory()
        ram = {
            "used": geter.used,
            "free": geter.available,
            "all": geter.total
        }
        return ram
    def getswap(self) -> dict:
        geter = psutil.swap_memory()
        swap = {
            "used": geter.used,
            "free": geter.free,
            "all": geter.total
        }
        return swap
class PlatFormInfo:
    def __init__(self):
        pass
    def get(self):
        pydict = {
            "vers": platform.python_version(),
            "pybuild": platform.python_build()
        }
        infodict = {
            "os": platform.system(),
            "vers": platform.version(),
            "release": platform.release(),
            "oses": {
                "win": psutil.WINDOWS,
                "linux": psutil.LINUX,
                "macos": psutil.MACOS
            }
        }
        dicter = {
            "py": pydict,
            "info": infodict
        }
        return dicter


class monitor:
    def __init__(self, fps):
        with rich.live.Live('', refresh_per_second=max(2, min(fps, 60))) as live:
            try:
                while True:
                    "#00fffb" #! не трогать! hex не отображается без этого
                    ram = ramInfo().getram()
                    swap = ramInfo().getswap()
                    info = PlatFormInfo().get()
                    live.update(
                        f'''
[#008cff]-------- RAM / SWAP --------[/]
[#008cff]Ram-USED: {ram["used"] / (1024 ** 3):.6f} GB
[#008cff]Ram-FREE: {ram["free"] / (1024 ** 3):.6f} GB
[#008cff]Ram-TOTAL: {ram["all"] / (1024 ** 3):.6f} GB
[#00fffb]SWAP-USED: {swap["used"] / (1024 ** 3):.6f} GB
[#00fffb][#00fffb]SWAP-FREE: {swap["free"] / (1024 ** 3):.6f} GB
[#00fffb]SWAP-TOTAL: {swap["all"] / (1024 ** 3):.6f} GB
[#48ff00]--------- PLATFORM ----------[/]
[#48ff00]os: {info["info"]["os"]} {info["info"]['release']}
[#48ff00]version: {info['info']['vers']}
[#48ff00]release: {info["info"]['release']}
[#48ff00]---------------
[#48ff00]WINDOWS?: {info["info"]["oses"]["win"]}
                        '''
                    )
            except KeyboardInterrupt:
                print('done')
                return
            except Exception as e:
                print(f'возникла ошибка: {e}')
                return

monitor(fps=30)