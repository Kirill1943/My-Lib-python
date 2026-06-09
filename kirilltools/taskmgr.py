import platform as _platform, psutil as _psutil
import rich.live
import time as _time
import kirilltools.errors.math as _err
import os as _os
import GPUtil as _GPUtil

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

class WebInfo:
    def __init__(self) -> None:
        self.last_net = _psutil.net_io_counters()
        self.last_time = _time.perf_counter()

    def get_network_speed(self) -> dict:
        current_net = _psutil.net_io_counters()
        current_time = _time.perf_counter()
        time_delta = current_time - self.last_time
        
        if time_delta <= 0:
            return {"download_mb": 0.0, "upload_mb": 0.0}
            
        download_bytes = current_net.bytes_recv - self.last_net.bytes_recv
        send_bytes = current_net.bytes_sent - self.last_net.bytes_sent
        
        megabits_recv = (download_bytes / (1024 ** 2)) / time_delta
        megabits_sent = (send_bytes / (1024 ** 2)) / time_delta
        
        self.last_net = current_net
        self.last_time = current_time
        
        return {
            "download_mb": round(megabits_recv, 2),
            "upload_mb": round(megabits_sent, 2)
        }
    def get_errors_drops(self) -> dict:
        net = _psutil.net_io_counters()
        return {
            "err": {
                "in": net.errin,
                "out": net.errout
            },
            "drop": {
                "in": net.dropin,
                "out": net.dropout
            }
        }
    def get_adapters(self) -> dict:
        interfaces = _psutil.net_if_addrs()
        stats = _psutil.net_if_stats()
        adapters_dict = {}

        for interface_name, addresses in interfaces.items():
            is_active = stats[interface_name].isup if interface_name in stats else False
            
            if not is_active:
                continue
            adapters_dict[interface_name] = {
                "active": is_active,
                "ipv4": None,
                "ipv6": None,
                "mac": None
            }

            for addr in addresses:
                if addr.family == _psutil.AF_LINK:
                    adapters_dict[interface_name]["mac"] = addr.address
                elif addr.family == 2:
                    adapters_dict[interface_name]["ipv4"] = addr.address
                elif addr.family == 23:
                    adapters_dict[interface_name]["ipv6"] = addr.address

        return adapters_dict

class CpuInfo:
    def __init__(self) -> None:
        self.logic_cores = _psutil.cpu_count(logical=True)
        self.realy_cores = _psutil.cpu_count(logical=False)
    def get_freq(self) -> dict:
        dict_ = {
            "max GHz": "?",
            "Now GHz": "?"
        }
        try:
            freq = _psutil.cpu_freq()
            if freq:
                dict_ = {
                    "max GHz": freq.current / 1000,
                    "Now GHz": freq.max / 1000
                }
        except Exception:
            pass
        return dict_
    def get_load(self) -> float:
        return _psutil.cpu_percent(interval=None)

class GpuInfo:
    def __init__(self):
        pass
    def get(self) -> list:
        gpus = _GPUtil.getGPUs()
        list_ = []

        for gpu in gpus:
            list_.append( # Исправили list на list_
                {
                    "model": gpu.name,
                    "load": round(gpu.load * 100, 1),
                    "MemoryALL": gpu.memoryTotal, # Всего памяти на карте
                    "MemoryUsed": gpu.memoryUsed,   # Исправили имя ключа на понятное
                    "temperature": gpu.temperature
                }
            )

        return list_
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
                WebClass = WebInfo()
                CoreClass = CpuInfo()
                Gpuclass = GpuInfo()
                while True:
                    ram = ramclass.getram()
                    swap = ramclass.getswap()
                    info = platformclass.get()
                    battery = batteryclass.get()
                    disks = Diskclass.get()
                    isbatt = battery["battery?"]
                    network_speed = WebClass.get_network_speed()
                    network_droperr = WebClass.get_errors_drops()
                    adapters = WebClass.get_adapters()
                    Gpus = Gpuclass.get()
                    Gpus_line = []
                    disks_line = []
                    for part_key in disks.keys():
                        part_data = disks[part_key]
                        disks_line.append(
                            f"{part_data['mountpoint']}: Раздел {part_data['mountpoint']} "
                            f"Всего: {part_data['totalGB']:.2f} GB, "
                            f"занято: {part_data['UsageGB']:.2f} GB, "
                            f"свободно: {part_data['FreeGB']:.2f} GB"
                        )
                    if not Gpus:
                        Gpus_line.append("[#ff0000]Видеокарты не обнаружены или не поддерживаются[/]")
                    else:
                        for gpu in Gpus:
                            Gpus_line.append(
                                f"[#B6B300]🎮 Модель:[/] {gpu['model']}\n"
                                f"[#B6B300]📊 Нагрузка чипа:[/] {gpu['load']}% | [#B6B300]🌡️ Temp:[/] {gpu['temperature']} °C\n"
                                f"[#B6B300]💾 Видеопамять:[/] {gpu['MemoryTOTAL']} МБ / {gpu['MemoryALL']} МБ"
                            )
                    live.update(
                        f'''
[#008cff]-------- RAM / SWAP --------[/]
[#008cff]использовано ОЗУ: {ram["used"] / gb:.6f} GB, свободно ОЗУ: {ram["free"] / gb:.6f} GB, всего ОЗУ: {ram["all"] / gb:.6f} GB
[#00fffb]использовано СВОП: {swap["used"] / gb:.6f} GB, свободно СВОП: {swap["free"] / gb:.6f} GB, всего СВОП: {swap["all"] / gb:.6f} GB
[#48ff00]--------- PLATFORM ----------[/]
[#48ff00]ос: {info["info"]["os"]} {info["info"]['release']}
[#48ff00]версия (сборка): {info['info']['vers']}
[#48ff00]релиз: {info["info"]['release']}
[#48ff00]---------------
[#48ff00]Виндолс?: {info["info"]["oses"]["win"]}, Линукс?: {info["info"]["oses"]["linux"]}
[#48ff00]Мак Ос?: {info["info"]["oses"]['macos']}, Собственная ос?: {not info["info"]["oses"]["win"] and not info["info"]["oses"]["linux"] and not info["info"]["oses"]["macos"]}
[#c8ff00]-------- BATTERY --------[/]
[#c8ff00]батарея есть?: {isbatt}
[#c8ff00]количество %: {battery["заряд %"] if isbatt else None}
[#c8ff00]осталось до разряда батареи: {battery['осталось до разряда'] if isbatt else None}
[#c8ff00]заряжается?: {battery["заряжается?"] if isbatt else None}
[#ff0000]-------- DISKS / ДИСКИ --------[/]
[#ff0000]{"\n".join(disks_line)}
[#00B0DC]-------- WEB / NET / СЕТЬ --------[/]
[#0000FF]Скачивание: {(download := network_speed["download_mb"]):.2f} Mb/s | {round(download * 8, 2)} Mbps
[#FF0000]Отправка: {(upload := network_speed["upload_mb"]):.2f} Mb/s | {round(upload * 8, 2)} Mbps
[#FF0000]Битые пакеты от сервера: {network_droperr["err"]["in"]} Битые пакеты от устройства: {network_droperr["err"]["out"]}
[#FF8800]Дропнутые пакеты устройством (из сети): {network_droperr["drop"]["in"]}
[#FF8800]не отправленные пакеты: {network_droperr["drop"]["out"]}
[#00B0DC]-------- WEB / NET / СЕТЬ - СЕТИ --------[/]
{"\n".join([f"[#00B0DC]📡 {name} | Активен: {data['active']} | IP: {data['ipv4']} | MAC: {data['mac']}" for name, data in adapters.items() if data['ipv4']])}
[#FFFEB2]-------- CORE / ПРОЦЕССОР --------[/]
[#FFFEB2]физические ядра / логические ядра (потоки): {CoreClass.realy_cores} / {CoreClass.logic_cores}
[#FFFEB2]Текущая нагрузка: {CoreClass.get_load():.1f}%
[#B6B300]-------- GPU / ВИДЕОКАРТА --------[/]
[#B6B300]{"\n".join(Gpus_line)}
                        '''
                    )
                    _time.sleep(1 / self.fps)
            except KeyboardInterrupt:
                print('done')
                return
            except Exception as e:
                print(f'возникла ошибка: {e}')
                return

if __name__ == "__main__":
    monitor(fps=60).run()
__all__ = [
    "monitor", "ramInfo",
    "BatteryInfo", "PlatFormInfo", "DiskInfo", "WebInfo", "CpuInfo", "GpuInfo"
]