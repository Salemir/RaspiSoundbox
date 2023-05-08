from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import subprocess
from time import sleep

IdTrack001 = 30681865463
IdTrack002 = 762571267562

def play_mp3(file_path):
    subprocess.run(["mpg123", file_path])

while True:
    try:
        reader=SimpleMFRC522()

        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id = reader.read()[0]
            print("Card Value is:",id)

            if (id == IdTrack001):
            
                mp3_file_path = "/raspitracks/Track001.mp3"
                play_mp3(mp3_file_path)
                sleep(2)
                
            elif (id == IdTrack002):
                
                # playing an album
                mp3_file_path = "/raspitracks/Track002.mp3"
                play_mp3(mp3_file_path)
                sleep(2)
                
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()

