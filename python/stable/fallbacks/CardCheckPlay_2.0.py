#Version 2.0
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import subprocess
import threading
import time
import csv

csv_file_path = '/raspitracks/trackverz.CSV'

#TrackID und StopID Definition
with open(csv_file_path) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        name = row['IdTrack']
        value = int(row['ID'])
        globals()[name] = value 

#Suchfunktion in CSV nach IDs
def search_csv(csv_file_path, searchvar):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        header = next(csv_reader) # skip header row
        for row in csv_reader:
            if row[1].strip() == searchvar.strip():
                return row[3] # return the value in the second column of the matching row
        return 999

#Start von MP3
def play_mp3(file_path):
    subprocess.run(["mpg123", file_path])

#Check ob MP3 gespielt wird
def is_mpg123_playing():
    try:
        subprocess.check_output(['pidof', 'mpg123'])
        return True
    except subprocess.CalledProcessError:
        return False

#Erstdefinition der Variablen
playcheckvar = 1
checkvar = 1
id = 0

while True:
    try:
        print('Los gehts, Chip auflegen!')
        reader = SimpleMFRC522()        
        
        while True:
            #WENN ein neuer Chip aufgelegt wurde
            if id != checkvar:
                id = reader.read()[0]
                checkvar = id
                searchvar = str(id)
                
                #WENN Stop-Tags aufgelegt werden
                if id == IdStop1 or id == IdStop2:
                    subprocess.run(["killall", "mpg123"])
                    mp3_file_path = None
                    playcheckvar = 0
                    time.sleep(2)
                
                #WENN ein Tag aufgelegt wird welcher in der CSV gefunden wird
                elif (id != IdStop1 or id != IdStop2) and search_csv(csv_file_path, searchvar) != 999:
                    searchvar = str(id)
                    mp3_file_path = search_csv(csv_file_path, searchvar)
                    print(mp3_file_path)
                    #WENN gespielt wird beende den Track (zur Sicherheit)
                    if playcheckvar != 0:
                        subprocess.run(["killall", "mpg123"])
                        playcheckvar = 0

                    #starte den Song in einem Hintergrundprozess
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()
                    
                    playcheckvar = 1                    
                
                #WENN der Tag nicht in der CSV gefunden wird
                elif search_csv(csv_file_path, searchvar) == 999:
                    time.sleep(3)
                    
            
            #WENN der gleiche Chip aufgelegt ist wie zuvor UND der Player spielt: mach nix und check ob das noch so ist
            elif id == checkvar and is_mpg123_playing() is True:                            
                time.sleep(3)
                id = reader.read()[0]
            
            #WENN der gleiche Chip aufgelegt ist wie zuvor UND der Player NICHT spielt: gib die Wiedergabe für den gleichen RFID Tag wieder frei
            elif id == checkvar and is_mpg123_playing() is False:
                 checkvar = 0
            

    #WENN ein Fehler auftritt überspringe diesen und starte den Code neu
    except Exception as e:
        print(e)
        pass

    finally:
        print("GPIO cleanen")
        GPIO.cleanup()



