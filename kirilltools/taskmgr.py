import platform as _platform, psutil as _psutil
import rich.live
import time as _time
from kirilltools.errors import math as _err
import os as _os

class ramInfo:
    def __init__(self) -> None:
        pass
    def getram(self) -> dict:
        geter = _psutil.virtual_memory()
        ram = {
            "used": geter.used,
            "free": geter.available,
            "all": geter.total
        }
        return ram
    def getswap(self) -> dict:
        geter = _psutil.swap_memory()
        swap = {
            "used": geter.used,
            "free": geter.free,
            "all": geter.total
        }
        return swap
class BatteryInfo:
    def __init__(self) -> None:
        pass
    def isbattery(self) -> bool:
        return _psutil.sensors_battery() is None
    def getpowertime(self, seconds) -> str:
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
    def get(self) -> bool:
        battery = {"battery?": False}
        if not self.isbattery():
            info = _psutil.sensors_battery()
            s = info.secsleft
            battery["battery?"] = True
            battery["заряд %"] = info.percent
            if s == _psutil.POWER_TIME_UNLIMITED:
                battery["осталось до разряда"] = float('inf')
            elif s == _psutil.POWER_TIME_UNKNOWN:
                battery['осталось до разряда'] = "?"
            else:
                battery["осталось до разряда"] = self.getpowertime(s)
            battery["заряжается?"] = info.power_plugged
        return battery
class PlatFormInfo:
    def __init__(self) -> None:
        pass
    def get(self) -> dict:
        pydict = {
            "vers": _platform.python_version(),
            "pybuild": _platform.python_build()
        }
        infodict = {
            "os": _platform.system(),
            "vers": _platform.version(),
            "release": _platform.release(),
            "oses": {
                "win": _psutil.WINDOWS,
                "linux": _psutil.LINUX,
                "macos": _psutil.MACOS
            }
        }
        dicter = {
            "py": pydict,
            "info": infodict
        }
        return dicter

class DiskInfo:
    def __init__(self) -> None:
        pass
    def get(self) -> dict:
        dict_ = {}
        for part in _psutil.disk_partitions(all=False):
            if _os.name == 'nt' and ('cdrom' in part.opts or not part.fstype):
                continue
            try:
                usage = _psutil.disk_usage(part.mountpoint)
                dict_[part.mountpoint] = {
                    "mountpoint": part.mountpoint,
                    "totalGB": usage.total / (1024 ** 3),
                    "UsageGB": usage.used / (1024 ** 3),
                    "FreeGB": usage.free / (1024 ** 3)
                }
            except (PermissionError, FileNotFoundError, OSError):
                continue
        return dict_

class monitor:
    def __init__(self, fps) -> None:
        try:
            fps = int(fps)
        except (ValueError, TypeError):
            raise _err.TypesError("ты указал не int в поле fps!")
        self.fps = max(2, min(fps, 60))
    def run(self) -> None:
        with rich.live.Live('', refresh_per_second=self.fps) as live:
            try:
                gb = 1024 ** 3
                ramclass = ramInfo()
                platformclass = PlatFormInfo()
                batteryclass = BatteryInfo()
                Diskclass = DiskInfo()
                while True:
                    ram = ramclass.getram()
                    swap = ramclass.getswap()
                    info = platformclass.get()
                    battery = batteryclass.get()
                    disks = Diskclass.get()
                    isbatt = battery["battery?"]
                    disks_line = []
                    for part_key in disks.keys():
                        part_data = disks[part_key]
                        disks_line.append(
                            f"{part_data['mountpoint']}: Раздел {part_data['mountpoint']} "
                            f"Всего: {part_data['totalGB']:.2f} GB, "
                            f"занято: {part_data['UsageGB']:.2f} GB, "
                            f"свободно: {part_data['FreeGB']:.2f} GB"
                        )
                    live.update(
                        f'''
[#008cff]-------- RAM / SWAP --------[/]
[#008cff]использовано ОЗУ: {ram["used"] / gb:.6f} GB
[#008cff]свободно ОЗУ: {ram["free"] / gb:.6f} GB
[#008cff]всего ОЗУ: {ram["all"] / gb:.6f} GB
[#00fffb]использовано СВОП: {swap["used"] / gb:.6f} GB
[#00fffb]свободно СВОП: {swap["free"] / gb:.6f} GB
[#00fffb]всего СВОП: {swap["all"] / gb:.6f} GB
[#48ff00]--------- PLATFORM ----------[/]
[#48ff00]ос: {info["info"]["os"]} {info["info"]['release']}
[#48ff00]версия (сборка): {info['info']['vers']}
[#48ff00]релиз: {info["info"]['release']}
[#48ff00]---------------
[#48ff00]Виндолс?: {info["info"]["oses"]["win"]}
[#48ff00]Линукс?: {info["info"]["oses"]["linux"]}
[#48ff00]Мак Ос?: {info["info"]["oses"]['macos']}
[#48ff00]Собственная ос?: {not info["info"]["oses"]["win"] and not info["info"]["oses"]["linux"] and not info["info"]["oses"]["macos"]}
[#c8ff00]-------- BATTERY ]--------[/]
[#c8ff00]батарея есть?: {isbatt}
[#c8ff00]количество %: {battery["заряд %"] if isbatt else None}
[#c8ff00]осталось до разряда батареи: {battery['осталось до разряда'] if isbatt else None}
[#c8ff00]заряжается?: {battery["заряжается?"] if isbatt else None}
[#ff0000]-------- DISKS / Диски --------[/]
[#ff0000]{"\n".join(disks_line)}
                        '''
                    )
                    _time.sleep(1 / self.fps)
            except KeyboardInterrupt:
                print('done')
                return
            except Exception as e:
                print(f'возникла ошибка: {e}')
                return

__all__ = [
    "monitor", "ramInfo",
    "BatteryInfo", "PlatformInfo", "DiskInfo"
]