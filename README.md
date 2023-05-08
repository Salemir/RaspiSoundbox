# RaspiSoundbox
No Tonie, no Bullshit

## Image auf SD-Karte spielen
Image via [Raspberry Pi Imager](https://www.raspberrypi.com/software/) herunterladen und auf SD-Karte spielen (Stand 05.05.2023: Raspberry PI OS Lite 64-bit)

Bei Möglichkeit während Installation gleich folgendes aktivieren/konfigurieren:
- Hostname (mit diesem kann dann via HOSTNAME.local die Konfigurationsseite des Geräts aufgerufen werden bzw. so kann via SSH auf Raspberry zugegriffen werden)
- SSH
- Benutzername & Passwort (Bsp: david, juer, etc.)
- WiFi
- Tastaturlayout

## Verkabelung des RFID-Scanners und Taster:
RFID-Scanner (Modul RC522):
- SDA -> GPIO8, Pin 24
- SCK -> GPIO11, Pin 23
- MOSI -> GPIO10, Pin 19
- MISO -> GPIO9, Pin 21
- IRQ -> NICHT ANGESCHLOSSEN
- GND -> GND, Pin 20
- RST -> GPIO23, Pin 16
- 3,3V -> 3V3 power, Pin 17

Lautstärkeregler und Ein-/Aus-Taster verkabeln
- Ein/Aus zwischen GPIO3 (Pin 5) und GND (Pin 6) 
- Vol - zwischen GPIO26 (Pin 37) und GND (Pin 39)
- Vol + zwischen GPIO16 (Pin 36) und GND (Pin 34)

## Raspberry in Betrieb nehmen
Zuvor beschriebenen SD-Karte in den entsprechenden Slot stecken

Mit Netzteil verbinden (CAVE: mind. 1,5A-USB-Netzteil)

WENN Hostname, WiFi und SSH im Zuge des Installationsvorgangs nicht aktiviert wurden:
- Tastatur anschließen
- Monitor anschließen
- Netzteil anschließen
- Installation abwarten
- Raspi Auf Raspberry einloggen mit zuvor vergebenem Login (falls noch kein Username vergeben wurde: default raspberry login ergoogeln)
- WLAN, SSH (Kommunikation mit PC/MAC) und SPI (GPIO-Port-Steuerung) aktivieren
```console
sudo raspi-config
```
#unter 1 System Settings -> S1: Wireless Lan konfigurieren
#unter 1 System Settings -> S4: Hostname wählen ("Name" im Netzwerk)
#unter 3 Interface Options -> I2: SSH enablen
#unter 3 Interface Options -> I4: SPI enablen
#unter 8 Update -> raspi-config aktualisieren



ifconfig

WENN Hostname, WiFi und SSH im Zuge des Installationsvorgangs bereits aktiviert wurden:
- via SSH verbinden (mit Freeware [Putty](https://putty.org/); entweder auf IP-Adresse oder hostname.local verbinden; Hostname ersetzen durch geändertem Wert aus Installationsprozess)
- WLAN, SSH (Kommunikation mit PC/MAC) und SPI (GPIO-Port-Steuerung) aktivieren
#commandzeilen
sudo raspi-config
#unter 3 Interface Options -> I4: SPI enablen
#unter 8 Update -> raspi-config aktualisieren

Wenn möglich fixe IP-Adresse im Netzwerk vergeben
- Üblicherweise hat der Router des WLAN-Netzes eine Konfigurationsseite welche man über einen Browser erreichen kann (Bsp: [router.asus.com]([router.asus.com](http://router.asus.com/)). Über diese sollte es mittels Benutzeroberfläche möglich sein den Player zu finden und eine fixe IP zu vergeben (Bsp: Jür: 192.168.1.232, David: 192.168.1.231).




```console
foo@bar:~$ whoami
foo
```




o) On Off Button und AutoShutdown nach 3 Stunden enablen:
#commandzeilen
sudo nano /etc/systemd/logind.conf
#Raute vor "HandlePowerKey=poweroff" löschen
sudo nano /boot/config.txt
#einfügen von folgender Zeile unter "Additional overlays and parameters..."
dtoverlay=gpio-shutdown
#commandzeilen
sudo nano /etc/rc.local
#hinzufügen von folgender Zeile direkt über "exit 0"
(sleep 10800 && sudo poweroff) &
sudo reboot

o) Via Terminal verbinden
#mit Freeware Putty

o) Python3 und mpg123 updaten/installieren
#commandzeilen
sudo apt-get install python3-dev python3-pip mpg123
sudo pip3 install spidev; sudo pip3 install mfrc522

o) Samba Dateishare einrichten (Quelle: https://www.raspberry-buy.de/Raspberry_Pi_Tutorial_Windows_Dateifreigabe_Samba_SMB_Server_Installation.html)
#commandzeilen
sudo mkdir -m 0755 /scripts; sudo mkdir -m 1777 /transfer
sudo apt-get install samba samba-common-bin; sudo apt-get install samba samba-common smbclient
sudo systemctl restart smbd
sudo service smbd status
#wenn "active (running)" in grün angezeigt wird ist alles im grünen Bereich
#commandzeilen
sudo nano /etc/samba/smb.conf
#in smb.conf ggf ändern von "workgroup = WORKGROUP" zu anderem Arbeitsgruppennamen (auf PC/MAC checken wie die Workgroup des Computers heißt)
#hinzufügen von folgendem Block ganz unten im File

[transfer]
comment = Für Übertragung von Scripts und sonstiger Daten auf den Raspi
path = /transfer
read only = no
browseable = yes
create mask = 1777

#commandzeilen
sudo systemctl restart smbd
sudo service smbd restart; sudo service nmbd restart
sudo service smbd status
sudo smbpasswd -a david
#PASSWORTWÄHLEN
sudo systemctl restart smbd
sudo service smbd restart; sudo service nmbd restart
sudo service smbd status

o) auf pc/mac Netzwerkadressen von /transfer als Ordner im Finder oder Dieser PC hinzufügen
#commandzeilen
ifconfig
#unter wlan0: ip-Adresse suchen und aufschreiben
#David: \\192.168.1.231\transfer -> IP Adresse je nach Ergebnis von ifconfig ändern bei Bedarf
#MAC: HIERWEẞICHNOCHNICHTWIEDASGEHT
Daten von Backup auf OneDrive (Raspihörbuch\Daten_Backup XXXXXX vX.X) auf /transfer bringen

o) Webserver aktivieren und NGINX/PHP konfigurieren:
#https://raspberrytips.com/nginx-on-raspberry-pi/
#7.4: das steht für die Version, kann sich also in zukünftigen Releases ändern
#commandzeilen
sudo apt install nginx; sudo apt install php-fpm
sudo reboot
sudo nano /etc/php/7.4/fpm/pool.d/www.conf -> listen = 9000 unter listen = /run/php/php7.4-fpm.sock dazuhauen
sudo nano /etc/nginx/sites-enabled/default -> index.php dazuhauen, index.nginx-debian.html löschen
#Weiters in ~/sites-enabled/default folgenden Zustand herstellen (bedeutet 4 Zeilen von RAUTE befreien):
        location ~ \.php$ {
                include snippets/fastcgi-php.conf;
        #
        #       # With php-fpm (or other unix sockets):
        #       fastcgi_pass unix:/run/php/php7.4-fpm.sock;
        #       # With php-cgi (or other tcp sockets):
                fastcgi_pass 127.0.0.1:9000;
        }

#mögliche Uploaddateigröße in php.ini und nginx.conf ändern:
sudo nano /etc/php/7.4/fpm/php.ini -> upload_max_filesize=200M UND post_max_size=201M
sudo nano /etc/nginx/nginx.conf -> client_max_body_size 200M; unter http-Sektion (bspw. unter Zeile  # server_name_in_redirect off;)
sudo service nginx restart; sudo service nginx status
#user david der Gruppe www-data hinzufügen:
#commandzeilen
sudo usermod -a -G www-data david
sudo chown -R www-data:www-data /var/www/html/raspitracks

o) Weboberfläche vorbereiten
#commandzeilen
sudo rm /var/www/html/index.nginx-debian.html
sudo cp -r /transfer/html/stable/* /var/www/html/
sudo mkdir -m 1777 /var/www/html/raspitracks
sudo chown -R www-data:www-data /var/www/html/raspitracks
sudo rm /var/www/html/index.nginx-debian.html
#unter /var/www/html befindet sich das Root-Verzeichnis der Website; mit IP.AD.RE.SSE im Browser kommt man auf IP.AD.RE.SSE/index.html
#trackverz.CSV über Weboberfläche in /raspitracks laden (mittels Upload)

o) Player-Scriptauf Raspi bringen und Autostart aktivieren
#stabiles Wiedergabescript muss wie folgt abgelegt sein: /transfer/python/stable/CardCheckPlay_stable.py
#commandzeilen
sudo cp /transfer/python/stable/CardCheckPlay_stable.py /scripts
sudo crontab -e
#option „nano“ wählen
#für aktivieren des Scripts bei Boot folgende Zeile ganz unten hinzufügen und speichern (so aktiviert man den Autostart des Scripts)
@reboot python3 /scripts/CardCheckPlay_stable.py &
#commandzeilen
sudo reboot 

o) Alles auf Raspi aktualisieren
#commandzeilen
sudo apt-get update; sudo apt-get upgrade; sudo apt-get dist-upgrade

o) Inbetriebnahme
#Lieder via Weboberfläche hochladen
#Liedernamen (inklusive .mp3) den Stickern zuordnen


Service und Updates
o) laufende HTML/PHP-Files liegen auf /var/www/html/
o) Extrahieren von Produktivfiles für Manipulation:
#commandzeilen
sudo cp /var/www/html/index.php /transfer/html/beta/; sudo cp /var/www/html/update_csv.php /transfer/html/beta/
#herumspielen und speichern
o) Returnieren von Testfiles nach erfolgter Manipulation:
#commandzeilen
sudo cp /transfer/html/beta/index.php /var/www/html/; sudo cp /transfer/html/beta/update_csv.php /var/www/html/
o) Versionshistorie unter /transfer/versionsinfo.txt
o) Update von Python-Script: ChardCheckPlay_stable.py aktualisieren und in /scripts kopieren 
#commandzeilen
sudo cp /transfer/python/stable/CardCheckPlay_stable.py /scripts
o) letzte Version 2.3
o) BEI MANIPULATION VON CardCheckPlay_stable.py zuerst laufenden Prozess beenden mit folgenden
#commandzeilen
ps aux | grep python3
sudo kill NUMMERNACHUSERVOMLAUFENDENZUKILLENDENSCRIPT
