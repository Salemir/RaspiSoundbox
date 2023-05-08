#Version 1.6
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import subprocess
import threading

IdTrack001 = 30681865463
IdTrack002 = 762571267562

def play_mp3(file_path):
    subprocess.run(["mpg123", file_path])

# initialize the currently playing track to None
current_track = None

while True:
    try:
        reader = SimpleMFRC522()

        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id = reader.read()[0]
            print("Card Value is:",id)

            if id == IdTrack001:
                mp3_file_path = "/raspitracks/Track001.mp3"

                # stop the currently playing track, if any
                if current_track is not None:
                    subprocess.run(["killall", "mpg123"])
                    current_track = None

                # create a thread to play the song in the background
                song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                song_thread.start()

                current_track = mp3_file_path

            elif id == IdTrack002:
                mp3_file_path = "/raspitracks/Track002.mp3"

                # stop the currently playing track, if any
                if current_track is not None:
                    subprocess.run(["killall", "mpg123"])
                    current_track = None

                # create a thread to play the song in the background
                song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                song_thread.start()

                current_track = mp3_file_path

            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
