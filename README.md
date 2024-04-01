# RaspiSoundbox
No Tonie, no Bullshit

## Bauteilliste
- Raspberry Pi (Bsp: [Raspberry Pi 3A+](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/))
- Micro SD-Karte nach Wahl (zumindest 16gb empfohlen)
- F -> F Jumper-Kabel (Bsp: 20cm bei [Semaf Electronics](https://electronics.semaf.at/Jumper-Wire-Female-to-Female-10Pin-20cm))
- Taster für Lauter/Leiser/Ein-Aus (Bsp: Taster bei [Semaf Electronics](https://electronics.semaf.at/navi.php?qs=taster))
- RFID-Sticker (Bsp: 100Stk. auf [Amazon](https://www.amazon.de/dp/B07GH1P2M5?psc=1&ref=ppx_yo2ov_dt_b_product_details))
- RC522 RFID-Leser (Bsp: [Amazon](https://www.amazon.de/s?k=rc522&ref=nb_sb_noss_2))
- Es empfielt sich ein extra Gehäuse MIT MÖGLICHKEIT DES ANSTECKENS VON KONNEKTOREN AUF DEN GPIO-PINS zu kaufen. Rund um dieses Gehäuse kann die Optik selbst kreiert werden (Bsp: [Gehäuse für Raspberry Pi 3A+](https://electronics.semaf.at/Coupe-Rainbow-Pibow-3-A-Coupe-for-Raspberry-Pi-3-A-))
- Empfehlung: Kühlkörper für Wärmeableitung (Bsp: [Raspishop](https://www.rasppishop.de/kuehlkoerper_2))
- evtl. Klinkenstecker-Verlängerung für Kabelführung in Gehäuse (Bsp: [Amazon](https://www.amazon.de/dp/B0052L7F3M?psc=1&ref=ppx_yo2ov_dt_b_product_details))
- evtl. Micro-USB-Verlängerung für Kabelführung in Gehäuse (Bsp: [Amazon](https://www.amazon.de/dp/B01M70N4B4?psc=1&ref=ppx_yo2ov_dt_b_product_details))

## 1. Image auf SD-Karte spielen
Image via [Raspberry Pi Imager](https://www.raspberrypi.com/software/) herunterladen und auf SD-Karte spielen (Stand 05.05.2023: Raspberry PI OS Lite 64-bit)

#### Bei Möglichkeit während Installation gleich folgendes aktivieren/konfigurieren:
- Hostname (mit diesem kann zu späterem Zeitpunkt via HOSTNAME.local die Konfigurationsseite des Geräts aufgerufen werden bzw. so kann via SSH auf Raspberry zugegriffen werden)
- SSH
- Benutzername & Passwort (Bsp: david, juer, etc.)
- WiFi
- Tastaturlayout

## 2. Verkabelung des RFID-Scanners und Taster:
Ein Schaltplan der Pins auf dem Raspberry findet sich im File [GPIO Raspberry.png](https://github.com/Salemir/RaspiSoundbox/blob/main/GPIO%20Raspberry.png)

#### RFID-Scanner (Modul RC522) anschließen:
- SDA -> GPIO8, Pin 24
- SCK -> GPIO11, Pin 23
- MOSI -> GPIO10, Pin 19
- MISO -> GPIO9, Pin 21
- IRQ -> NICHT ANGESCHLOSSEN
- GND -> GND, Pin 20
- RST -> GPIO23, Pin 16
- 3,3V -> 3V3 power, Pin 17

#### Lautstärkeregler und Ein-/Aus-Taster anschließen:
- Ein/Aus Taster zwischen GPIO3 (Pin 5) und GND (Pin 6) 
- Vol - Taster zwischen GPIO26 (Pin 37) und GND (Pin 39)
- Vol + Taster zwischen GPIO16 (Pin 36) und GND (Pin 34)

## 3. Raspberry in Betrieb nehmen
- Zuvor beschriebenen SD-Karte in den entsprechenden Slot stecken
- Mit Netzteil verbinden (CAVE: mind. 1,5A-USB-Netzteil)
- Audio-Out mittels Klinkenstecker an Boxen/Kopfhörer anschließen

### 3.A WENN Hostname, WiFi und SSH im Zuge des Installationsvorgangs nicht aktiviert wurden (ansonsten weiter mit 3.B):
- Tastatur und Monitor anschließen
- Netzteil anschließen und Installationsvorgang abwarten
- Auf Raspberry einloggen mit zuvor vergebenem Login (falls noch kein Username vergeben wurde: default raspberry login ergoogeln)
- WLAN, SSH (Kommunikation mit PC/MAC) und SPI (GPIO-Port-Steuerung) aktivieren
```console
sudo raspi-config
```
- unter "1 System Settings -> S1": Wireless Lan konfigurieren
- unter "1 System Settings -> S4": Hostname wählen ("Name" im Netzwerk)
- unter "3 Interface Options -> I2": SSH enablen ("Fernzugriff" auf Terminal)
- unter "3 Interface Options -> I4": SPI enablen (Steuerung via Taster ermöglichen)
- unter "8 Update": raspi-config aktualisieren
- raspi-config beenden

#### Überprüfen der Verbindungseinstellungen
```console
ifconfig
```
Unter <b>WLAN0</b> befindet sich bei aktiver WLAN-Verbingung eine gültige IP-Adresse (Bsp: 192.168.1.231)

Es macht Sinn, sich von nun an mit dem Freeware-Tool [Putty](https://putty.org/) mit dem Raspberry zu verbinden, dies ist jedoch optional und nur wegen Komfort empfohlen. Verbindung kann entweder auf <b>hostname.local</b> (Hostname ersetzen durch geändertem Wert aus Installationsprozess) oder der IP-Adresse des Raspberry erfolgen. Wenn die Variante über IP-Adresse bevorzugt wird, sollte man gewährleisten, dass im Netzwerk für dieses Gerät eine fixe IP-Adresse vergeben wird.

### 3.B WENN Hostname, WiFi und SSH im Zuge des Installationsvorgangs bereits aktiviert wurden:
- Mittels PC via SSH verbinden (mit Freeware [Putty](https://putty.org/); entweder auf IP-Adresse oder hostname.local verbinden; (Hostname ersetzen durch geändertem Wert aus Installationsprozess)
- WLAN, SSH (Kommunikation mit PC/MAC) und SPI (GPIO-Port-Steuerung) aktivieren
```console
sudo raspi-config
```
- unter 3 Interface Options -> I4: SPI enablen
- unter 8 Update -> raspi-config aktualisieren

#### Wenn möglich fixe IP-Adresse im Netzwerk vergeben
- Üblicherweise hat der Router des WLAN-Netzes eine Konfigurationsseite welche man über einen Browser erreichen kann (Bsp: [router.asus.com]([router.asus.com](http://router.asus.com/)). Über diese sollte es mittels Benutzeroberfläche möglich sein den Player zu finden und eine fixe IP zu vergeben (Bsp: 192.168.1.232, 192.168.1.231).

## 4. Poweroptionen konfigurieren
#### Nutzung des On-Off-Buttons ermöglichen:
```console
sudo nano /etc/systemd/logind.conf
```
Raute (#) vor folgendem Eintrag löschen
> HandlePowerKey=poweroff

File speichern und schließen. Dies erfolgt üblicherweise mit STRG+X -> Y
```console
sudo nano /boot/config.txt
```
Einfügen von folgender Zeile unter "Additional overlays and parameters..."
> dtoverlay=gpio-shutdown

File speichern und schließen. (STRG+X -> Y)
#### AutoShutdown nach 3 Stunden einstellen:
```console
sudo nano /etc/rc.local
```
Hinzufügen von folgender Zeile direkt über "exit 0"
> (sleep 10800 && sudo poweroff) &
```console
sudo reboot
```
File speichern und schließen. (STRG+X -> Y)
## 5. Python3 und mpg123 updaten/installieren
```console
sudo apt-get install python3-dev python3-pip mpg123
```
```console
sudo pip3 install spidev; sudo pip3 install mfrc522
```

## 6. Samba Dateishare einrichten
Quelle: https://www.raspberry-buy.de/Raspberry_Pi_Tutorial_Windows_Dateifreigabe_Samba_SMB_Server_Installation.html
```console
sudo mkdir -m 0755 /scripts; sudo mkdir -m 1777 /transfer
```
```console
sudo apt-get install samba samba-common-bin; sudo apt-get install samba samba-common smbclient
```
```console
sudo systemctl restart smbd; sudo service smbd status
```
Wenn "active (running)" in grün angezeigt wird ist alles im grünen Bereich
```console
sudo nano /etc/samba/smb.conf
```
#### Hinzufügen von folgendem Block ganz unten im File

> [transfer]

> comment = Für Übertragung von Scripts und sonstiger Daten auf den Raspi  
> path = /transfer  
> read only = no  
> browseable = yes  
> create mask = 1777

Falls die Arbeitsgruppe des Netzwerkes in welches der Raspberry anders lautet als WORKGROUP, ist dies ebenso in der Konfigurationsdatei smb.conf zu ändern. Der Eintrag der folgenden Zeile ist entsprechend anzupassen:
 > workgroup = WORKGROUP

File speichern und schließen. (STRG+X -> Y)
#### Neustarten und Überprüfen der Services:
```console
sudo systemctl restart smbd; sudo service smbd restart; sudo service nmbd restart; sudo service smbd status
```
#### Passwort für den Dateizugriff via PC konfigurieren
```console
sudo smbpasswd -a USERNAME
```
"USERNAME" ist durchen einen aktiven/dem zuvor gewählten Benutzernamen zu ersetzen.

#### Auf PC den Ordner /transfer im Windows Explorer hinzufügen
Auf Raspberry die IP-Adresse herausfinden
```console
ifconfig
```
Im Eintrag ``wlan0`` findet man die IP-Adresse. Hier am Beispiel von ``192.168.1.231``:
- In ExplorerArbeitsplatz/Dieser PC mit rechter Maustaste auf freie weiße Fläche klicken.
- ``Netzwerkadresse hinzufügen`` wählen.
- Benutzerdefinierte Adresse ``\\192.168.1.231\transfer`` einfügen
- Weiter und Ordner sinnvoll benennen (Bsp: ``RaspiSoundbox Transfer``)

#### WICHTIG: Alle Dateien aus dem Github-Ordner inklusive Unterordner sollten direkt den erstellten ``/transfer``-Ordner auf dem Raspberry kopiert werden. Ebenso müssen die Pfade exakt wie angegeben beibehalten werden.

## 7. Webserver aktivieren und NGINX/PHP konfigurieren
Quelle: https://raspberrytips.com/nginx-on-raspberry-pi/  
CAVE: ``7.4`` steht für die Version, kann sich also in zukünftigen Releases ändern

#### NGINX und PHP installieren

```console
sudo apt install nginx; sudo apt install php-fpm
```
```console
sudo reboot
```
#### NGINX und PHP konfigurieren
```console
sudo nano /etc/php/7.4/fpm/pool.d/www.conf
```
Unter dem Eintrag ``listen = /run/php/php7.4-fpm.sock`` den Eintrag``listen = 9000`` hinzufügen.
```console
sudo nano /etc/nginx/sites-enabled/default
```
Eintrag ``index.nginx-debian.html`` löschen, dafür ``index.php`` hinzufügen.

Ebenso ist folgender Zustand im File herzustellen (bedeutet 4 Zeilen von RAUTE befreien):

>        location ~ \.php$ {  
>                include snippets/fastcgi-php.conf;  
>        #  
>        #       # With php-fpm (or other unix sockets):  
>        #       fastcgi_pass unix:/run/php/php7.4-fpm.sock;  
>        #       # With php-cgi (or other tcp sockets):  
>                fastcgi_pass 127.0.0.1:9000;  
>        }
File speichern und schließen. (STRG+X -> Y)

#### Mögliche Uploaddateigrößen definieren
```console
sudo nano /etc/php/7.4/fpm/php.ini
```
Werte zu ``upload_max_filesize=200M`` und ``post_max_size=201M`` ändern.

File speichern und schließen. (STRG+X -> Y)
```console
sudo nano /etc/nginx/nginx.conf
```
Zeile ``client_max_body_size 200M;`` unter http-Sektion (bspw. unter Zeile  ``# server_name_in_redirect off;``) hinzufügen.

File speichern und schließen. (STRG+X -> Y)
```console
sudo service nginx restart; sudo service nginx status
```
#### Hauptuser der Gruppe www-data hinzufügen
```console
sudo usermod -a -G www-data USERNAME
```
"USERNAME" ist durch einen aktiven/dem zuvor gewählten Benutzernamen zu ersetzen.

## 8. Weboberfläche vorbereiten und Erstkonfiguration durchführen
```console
sudo rm /var/www/html/index.nginx-debian.html; sudo cp -r /transfer/html/stable/* /var/www/html/; sudo mkdir -m 1777 /var/www/html/raspitracks; sudo chown -R www-data:www-data /var/www/html/raspitracks
```
Unter ``/var/www/html`` befindet sich die Dateiablage für die Website der Player-Verwaltung (Trackzuordnung, Tracklöschung, etc.). Durch einen erstmaligen Aufruf der IP.AD.RE.SSE (ab dann via HOSTNAME.local möglich; HOSTNAME wurde am Anfang dieses Tutorials definiert) auf einem Browser eines Geräts im gleichen Netzwerk erreicht man die Playerverwaltung.

#### Trackverzeichnis implementieren
Die Datei ``trackverz.CSV`` zuerst auf einem PC bearbeiten (RFID-Nummern der jeweiligen Sticker/Karten/etc. eintragen und mit Kommentar versehen) über den Uploadbutton der Weboberfläche des Raspberrys uploaden und auf Upload/Refresh klicken.

Es macht Sinn, RFID-Tags als "Stop" zu definieren. Hierzu sind die beiden letzten Zeilen im File ``trackverz.CSV`` reserviert. Wenn man diese am PC öffnet wird die erste Spalte ersichtlich. Bei den "Stop"-Tags lautet die interne Bezeichnung "IdStop1" und "IdStop2". In der Weboberflächefinden sich die Zeilen dazu bei den Einträgen in der Spalte "Stickerbezeichnung" -> "Stop-RFID 1" und "Stop-RFID 2".

#### RFIDs lesen
Um RFID-Sticker/Karten/etc. zu lesen kann das ein spezielles Programm im Terminal aufgerufen werden:
```console
sudo python3 /transfer/python/stable/Lesegeraet_1.5.py
```
RFID-Tags können nacheinander aufgelegt werden, die RFID-Nummern werden nacheinander im Terminal angezeigt. Diese können für die Zuweisung direkt in die Weboberfläche wie oben beschrieben eingetragen werden. Selbstverständlich ist es möglich, die Datei ``trackverz.CSV`` direkt am PC gänzlich zu befüllen und diese über die Weboberfläche hochzuladen.

Das Programm lässt sich mit der Tastenkombination STRG+C beenden.

## 9. Player konfigurieren
Wie bereits zuvor geschrieben, die Dateistrukturen müssen wie angegeben existieren und die jeweiligen Dateien in diesen Strukturen abgelegt sein.
```console
sudo cp /transfer/python/stable/CardCheckPlay_stable.py /scripts; sudo crontab -e
```
Hier ist die Aktion ``nano`` zu wählen. Um den Autostart zu aktivieren ist folgende Zeile ganz unten im File hinzuzufügen:
> @reboot python3 /scripts/CardCheckPlay_stable.py &

File speichern und schließen. (STRG+X -> Y)
```console
sudo reboot 
```

## 10. System aktualisieren
```console
sudo apt-get update; sudo apt-get upgrade; sudo apt-get dist-upgrade
```
```console
sudo reboot 
```

## 11. Inbetriebnahme
- Lieder via Weboberfläche (erreichbar über IP.AD.RE.SSE oder HOSTNAME.local mit einem Browser auf einem Gerät im selben Netzwerk) hochladen. CAVE: Nach letztem Track ist nochmals ein Klick auf den "Upload/Refresh"-Button notwendig.
- Um konkrete Zuweisungen der Tracks zu den RFID-Stickern herzustellen ist der Trackname (inklusive .mp3) in das jeweilige Feld im linken Bereich der Website einzutragen. Am Ende der Liste findet sich der Button ``Änderungen speichern``.


## Z. Service und Updates

### Update der Programme

Um die konkreten Dateien upzudaten müssen die Dateien welche Vorversionen ersetzen sollen wie folgt abgelegt werden:
- Website-Files: ``/transfer/html/stable/index.php`` und ``/transfer/html/stable//update_csv.php``
- Player-File: ``/transfer/python/stable/CardCheckPlay_stable.py``

Um die Dateien an die jeweiligen Stellen auf dem Raspberry zu kopieren/diese upzudaten können folgende Befehle verwendet werden:

#### Website-Files:
```console
sudo cp /transfer/html/stable/index.php /var/www/html/; sudo cp /transfer/html/stable/update_csv.php /var/www/html/
```

#### Player-File:
- CAVE: Um ein sauberes Update durchzuführen muss der Prozess zuerst beendet werden. Dies erfolgt mit foldenden Terminal-Befehlen:
```console
ps aux | grep python3
```
```console
sudo kill ENTSPRECHENDEPROZESSNUMMERVONCARDCHECHPLAY_STABLE.PY
```
Das konkrete Update des Players wird mit folgendem Befehl ausgeführt:
```console
sudo cp /transfer/python/stable/CardCheckPlay_stable.py /scripts
```

### Extrahieren von Files für Manipulation/Troubleshooting:
Mit diesen Befehlen werden die Dateien in den Ordner ``/transfer/html/beta/`` bzw. ``transfer/python/beta`` kopiert.

- Websites-Files:
```console
sudo cp /var/www/html/index.php /transfer/html/beta/; sudo cp /var/www/html/update_csv.php /transfer/html/beta/
```
- Player-File:
```console
sudo cp /scripts/index.php /transfer/html/beta/
```

### Die Versionshistorie findet sich im File versionsinfo.txt
