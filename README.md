pi service dashboard runs a flask webapp that acts as a hub
for any web service running on the pi. This comes with
File Browser, Plex, and Pi-hole.

![Screenshot_20240413_091709_Chrome](https://github.com/MrLately/pi-service-dashboard/assets/94589563/36d53fcf-5eb1-4eaa-8476-be52cc164f43)


During the setup it asks you to select a drive. It will
WIPE AND FORMAT the drive to ext4 and mount it as the NAS
and Samba Share so you can also mount it from other
devices on your network. This setup assumes you have new
drive for nas and dont mind it being wiped. In the pic I'm
selecting /dev/sda bc thats the drive I'm wanting to wipe,
format, and mount as the shared drive (nas drive).

<img width="208" alt="sd" src="https://github.com/MrLately/pi-service-dashboard/assets/94589563/cb81cc74-3064-4f89-ab02-b9b909114e6f">


You can add more services by following the flow in config.json.
Add name and url and it will make a button for it in the homepage!
While your're there edit the username to your own.
Remember after any edits to run: sudo systemctl restart homepage.service

<img width="448" alt="gh" src="https://github.com/MrLately/pi-service-dashboard/assets/94589563/3d5f4320-2a3c-4426-8e48-bc05baf1e75a">

Installation:

https://youtu.be/I0vmhCSVJdc?si=8_aEeWgAN5-MrJO9

sudo apt install git -y

git clone https://github.com/MrLately/pi-service-dashboard

cd pi-service-dashboard

cd pihome

chmod +x setup.sh

sudo ./setup.sh

Follow prompts for selecting drive and setting up pihole.

pi_ip:5000 in the browser

USE:

Add bookmark or pwa to homescreen depending on mobile os. In
the video above I show how to do it on Android so that it acts 
as a standalone app.

Can add the shared folder to "network storage" on just about any mobile or desktop environment. 
android
iphone
windows
mac


