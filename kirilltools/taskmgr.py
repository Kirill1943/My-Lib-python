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
class BatteryInfo:
    def __init__(self):
        pass
    def isbattery(self):
        return psutil.sensors_battery() is None
    def getpowertime(self, seconds):
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        parts = []
        if days > 0: parts.append(f"{days}д")
        if hours > 0: parts.append(f"{hours}ч")
        if minutes > 0: parts.append(f"{minutes}м")
        if secs > 0 or not parts: parts.append(f"{secs}с")
        return " ".join(parts)
    def get(self):
        battery = {"battery?": False}
        if not self.isbattery():
            info = psutil.sensors_battery()
            s = info.secsleft
            battery["battery?"] = True
            battery["заряд %"] = info.percent
            if s == psutil.POWER_TIME_UNLIMITED:
                battery["осталось до разряда"] = float('inf')
            elif s == psutil.POWER_TIME_UNKNOWN:
                battery['осталось до разряда'] = "?"
            else:
                battery["осталось до разряда"] = self.getpowertime(s)
        return battery
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
                ramclass = ramInfo()
                platformclass = PlatFormInfo()
                batteryclass = BatteryInfo()
                while True:
                    ram = ramclass.getram()
                    swap = ramclass.getswap()
                    info = platformclass.get()
                    battery = batteryclass.get()
                    isbatt = battery["battery?"]
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
[#48ff00]LINUX?: {info["info"]["oses"]["linux"]}
[#48ff00]MACOS?: {info["info"]["oses"]['macos']}
[#c8ff00]-------- BATTERY ]--------[/]
[#c8ff00]is battery?: {isbatt}
[#c8ff00]количество %: {battery["заряд %"] if isbatt else None}
[#c8ff00]осталось до разряда батареи: {battery['осталось до разряда'] if isbatt else None}
                        '''
                    )
            except KeyboardInterrupt:
                print('done')
                return
            except Exception as e:
                print(f'возникла ошибка: {e}')
                return