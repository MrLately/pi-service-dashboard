pi service dashboard runs a flask webapp that acts as a hub
for any web service running on the pi. This comes with
File Browser, Plex, and Pi-hole.

During the setup it asks you to select a drive. It will
WIPE AND FORMAT the drive to ext and mount it as the NAS
and Samba Share so you can also mount it from other
devices on your network. This setup assumes you have new
drive for nas and dont mind it being wiped.

You can add more services by following the flow in config.json.
add name and url and it will make a button for it in the homepage!
Can be local or not, doesn't matter.

https://youtu.be/I0vmhCSVJdc?si=8_aEeWgAN5-MrJO9

sudo apt install git -y

git clone https://github.com/MrLately/pi-service-dashboard

cd pi-service-dashboard

cd pihome

chmod +x setup.sh

sudo ./setup.sh

Follow prompts for selecting drive and setting up pihole.

pi_ip:5000 in the browser

