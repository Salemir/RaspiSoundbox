# Version 2.3
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import subprocess
import threading
import time
import csv
import os

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set pin numbers for volume up and volume down buttons
VOLUME_UP_PIN = 16
VOLUME_DOWN_PIN = 26

# Set initial volume to 50%
volume = 90

# Set the command to adjust the volume
def set_volume(vol):
    os.system(f'amixer -c 0 sset PCM {vol}% > /dev/null')

# Function to handle the volume up button press
def volume_up_callback(channel):
    global volume
    if volume < 100:
        volume += 5
        set_volume(volume)

# Function to handle the volume down button press
def volume_down_callback(channel):
    global volume
    if volume > 0:
        volume -= 5
        set_volume(volume)

# Set up GPIO pins for input without pull-up resistors
GPIO.setup(VOLUME_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOLUME_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Add event listeners for the volume up and down buttons
GPIO.add_event_detect(VOLUME_UP_PIN, GPIO.FALLING, callback=volume_up_callback, bouncetime=200)
GPIO.add_event_detect(VOLUME_DOWN_PIN, GPIO.FALLING, callback=volume_down_callback, bouncetime=200)

# Initiale Lautstärke und CSV-Pfad definieren
set_volume(volume)
csv_file_path = '/var/www/html/raspitracks/trackverz.CSV'

# TrackID und StopID Definition via CSV
with open(csv_file_path) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        name = row['IdTrack']
        value = int(row['RFID'])
        globals()[name] = value


# Suchfunktion in CSV nach IDs
def search_csv(pfad, suchvariable):
    with open(pfad, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        header = next(csv_reader)  # skip header row
        for row in csv_reader:
            if row[1].strip() == suchvariable.strip():
                return row[3]  # return the value in the second column of the matching row
        return 999


# Startfunktion von MP3
def play_mp3(file_path):
    subprocess.run(["mpg123", file_path])


# Checkfunktion ob MP3 gespielt wird
def is_mpg123_playing():
    try:
        subprocess.check_output(['pidof', 'mpg123'])
        return True
    except subprocess.CalledProcessError:
        return False


# Erstdefinition der Variablen für die RFID-Reader-Lesevorgänge
# Playcheckvar wird nur zwischen 1 und 0 umgestellt
# Checkvar zwischen 0 und Wert von RFID-Tag
# rfid ist immer der Wert von letztmalig gelesenem RFID-Tag
playcheckvar = 0
checkvar = 0
path = "/var/www/html/raspitracks/"
trackname = None
rfid = 99

while True:
    try:
        print('Los gehts, Chip auflegen!')
        reader = SimpleMFRC522()

        while True:
            # WENN ein neuer Chip aufgelegt wurde
            if rfid != checkvar:
                rfid = reader.read()[0]
                checkvar = rfid
                searchvar = str(rfid)

                # WENN Stop-Tags aufgelegt werden
                if rfid == IdStop1 or rfid == IdStop2:
                    subprocess.run(["killall", "mpg123"])
                    mp3_file_path = None
                    playcheckvar = 0
                    time.sleep(2)

                # WENN ein Tag aufgelegt wird welcher in der CSV gefunden wird
                elif (rfid != IdStop1 or rfid != IdStop2) and search_csv(csv_file_path, searchvar) != 999:
                    searchvar = str(rfid)
                    trackname = search_csv(csv_file_path, searchvar)
                    mp3_file_path = path + trackname
                    print(mp3_file_path)
                    # WENN gespielt wird, beende den Track (zur Sicherheit)
                    if playcheckvar != 0:
                        subprocess.run(["killall", "mpg123"])
                        playcheckvar = 0

                    # starte den Song in einem Hintergrundprozess
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    playcheckvar = 1

                # WENN der Tag nicht in der CSV gefunden wird
                elif search_csv(csv_file_path, searchvar) == 999:
                    time.sleep(3)


            # WENN der gleiche Chip aufgelegt ist wie zuvor UND der Player spielt:
            # Mache nichts und check nach 3 Sekunden nochmal
            elif rfid == checkvar and is_mpg123_playing() is True:
                time.sleep(3)
                rfid = reader.read()[0]

            # WENN der gleiche Chip aufgelegt ist wie zuvor UND der Player NICHT spielt:
            # gib die Wiedergabe für den gleichen RFID-Tag wieder frei
            elif rfid == checkvar and is_mpg123_playing() is False:
                checkvar = 0


    # WENN ein Fehler auftritt, überspringe diesen und starte den Code neu
    except Exception as e:
        print(e)
        pass

    finally:
        print("GPIO cleanen")
        GPIO.cleanup()
