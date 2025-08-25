# Linux System Monitor Dashboard

A live system monitoring web dashboard built with Python, Flask, and Chart.js.  
Displays CPU, memory, disk usage, uptime, and the top 5 processes by memory usage in real-time.

## Features

- System information (OS, release, uptime)
- CPU, memory, and disk usage
- Live CPU usage chart (updates every 2 seconds)
- Top 5 processes table (by memory usage)
- JSON API endpoint (`/api/stats`)
- Runs locally on Debian-based Linux systems
- Easy to deploy as a background service (systemd)

## Screenshots

![Dashboard Screenshot](screenshots/dashboard.png)

## Installation

1. Clone the repository:
git clone https://github.com/RoyceBanks/linux-system-monitor.git

cd linux-system-monitor

2. Install dependencies:
pip3 install -r requirements.txt

3. Run the app:
python3 monitor_web.py

4. Open your browser at:
http://localhost:5000

## License
This project is licensed under the [MIT License](LICENSE).
