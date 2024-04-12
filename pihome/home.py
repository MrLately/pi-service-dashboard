from flask import Flask, render_template
import psutil
import shutil
import json

app = Flask(__name__)

with open('/home/pi/pi-service-dashboard/home_os/config.json') as config_file:
    config = json.load(config_file)
user_name = config.get('user_name', 'User')
services = config.get('services', [])
drives = config.get('drives', [])

@app.route('/')
def home():
    #system metrics
    cpu_load = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)

    #drive metrics
    drive_metrics = []
    for drive in drives:
        usage = shutil.disk_usage(drive['mount_point'])
        drive_metrics.append({
            'label': drive['label'],
            'used': usage.used / (1024 ** 3),
            'total': usage.total / (1024 ** 3)
        })

    return render_template('index.html', user_name=user_name, services=services, cpu_load=cpu_load,
                           ram_used=ram_used, ram_total=ram_total, drive_metrics=drive_metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

