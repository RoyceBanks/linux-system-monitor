import psutil
import platform
import datetime

def get_system_info():
    info = {}

    # System basics
    info['system'] = platform.system()
    info['release'] = platform.release()
    info['uptime'] = str(datetime.timedelta(seconds=int(psutil.boot_time())))

    # CPU
    info['cpu_percent'] = psutil.cpu_percent(interval=1)
    info['cpu_cores'] = psutil.cpu_count(logical=True)

    # Memory
    mem = psutil.virtual_memory()
    info['memory_total'] = round(mem.total / (1024 ** 3), 2)
    info['memory_used'] = round(mem.used / (1024 ** 3), 2)
    info['memory_percent'] = mem.percent

    # Disk
    disk = psutil.disk_usage('/')
    info['disk_total'] = round(disk.total / (1024 ** 3), 2)
    info['disk_used'] = round(disk.used / (1024 ** 3), 2)
    info['disk_percent'] = disk.percent

    # Processes (top 5 by memory)
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        processes.append(proc.info)
    top_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]
    info['top_processes'] = top_processes

    return info

if __name__ == "__main__":
    stats = get_system_info()
    for key, value in stats.items():
        print(f"{key}: {value}")
