from flask import Flask, render_template, jsonify
import psutil
import platform
import datetime

app = Flask(__name__)

def get_stats():
    stats = {}

    # System info
    stats['system'] = platform.system()
    stats['release'] = platform.release()

    # Uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    stats['uptime'] = str(uptime).split('.')[0]  # strip microseconds

    # CPU, Memory, Disk
    stats['cpu_percent'] = psutil.cpu_percent(interval=1)
    stats['memory_percent'] = psutil.virtual_memory().percent
    stats['disk_percent'] = psutil.disk_usage('/').percent

    # Top 5 processes by memory usage
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)
    stats['top_processes'] = processes[:5]

    return stats

# JSON API endpoint
@app.route('/api/stats')
def api_stats():
    return jsonify(get_stats())

# Dashboard frontend
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    # host=0.0.0.0 allows access from other devices on the network
    app.run(host='0.0.0.0', port=5000, debug=False)
