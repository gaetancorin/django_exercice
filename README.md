- Create a VM with image debian11 Serveur (64bits)
- Activate network access mode "réseau privé hôte" VirtualBox Host-Only Ethernet Adapter

-connect at user (in example, user is "osboxes")

[CMD]- sudo apt update

[CMD]- sudo apt install python3.9

[CMD]- sudo apt install python3-pip

[CMD]- pip3 install Django

[CMD]- sudo apt install git

[CMD]- sudo apt install scapy

[CMD]- git clone https://github.com/gaetancorin/django_exercice.git

[CMD]- sudo python3 django_exercice/monsite/manage.py runserver 0.0.0.0:8000

On your host computer, Go to http://192.168.56.12:8000/sondage/ (need 30s to download all sniff, just wait)
