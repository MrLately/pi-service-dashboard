Pi Service Dashboard
The Pi Service Dashboard runs a Flask web app that serves as a hub for any web service running on the Raspberry Pi. This setup includes services like File Browser, Plex, and Pi-hole.

Dashboard Screenshot

Drive Setup
During the setup, you will be prompted to select a drive. This process will WIPE AND FORMAT the drive to ext4 and mount it as the NAS and Samba Share. This allows it to be mounted from other devices on your network. This setup assumes you have a new drive for NAS and don't mind it being wiped. In the picture below, I'm selecting /dev/sda because that's the drive I want to wipe, format, and mount as the shared drive (NAS drive).

Drive Selection

Installation
Watch the Installation Video:

Setup Video Guide
Install the necessary tools and clone the repository:

bash
Copy code
sudo apt install git -y
git clone https://github.com/MrLately/pi-service-dashboard
cd pi-service-dashboard/pihome
chmod +x setup.sh
sudo ./setup.sh
Follow the on-screen prompts to select the drive and setup Pi-hole.

Access the dashboard:

Navigate to pi_ip:5000 in your web browser to access the dashboard.
Usage
Mobile Integration:

Add a bookmark or PWA to your homescreen depending on your mobile OS. The installation video shows how to do this on Android, enabling it to act as a standalone app.
Network Storage:

The shared folder can be added to "network storage" on nearly any mobile or desktop environment, including Android, iPhone, Windows, and Mac.
Adding More Services
You can add more services by following the flow in config.json. Add a name and URL, and it will create a button for it on the homepage! While you're there, edit the username to your own.

Important:
Remember, after any edits to config.json, you must run:

bash
Copy code
sudo systemctl restart homepage.service
Config Example



