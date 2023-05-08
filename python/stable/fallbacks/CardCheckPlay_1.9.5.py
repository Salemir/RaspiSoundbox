#Version 1.9.5
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import subprocess
import threading
import time
import csv

with open('/raspitracks/trackverz.CSV') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        name = row['IdTrack']
        value = int(row['ID'])
        globals()[name] = value 


def play_mp3(file_path):
    subprocess.run(["mpg123", file_path])

def is_mpg123_playing():
    try:
        subprocess.check_output(['pidof', 'mpg123'])
        return True
    except subprocess.CalledProcessError:
        return False

# Erstdefinition der Variable current_track
current_track = None
checkvar = None
id = 1


while True:
    try:
        reader = SimpleMFRC522()        
        
        while True:
            #WENN ein neuer Chip aufgelegt wurde
            if id != checkvar:
                
                print("Ich warte auf einen RFID-Scan")
                id = reader.read()[0]
                print("Du hast folgenden RFID-Tag gelesen:",id)
                checkvar = id
                
                if id == IdStop1 or id == IdStop2:
                    subprocess.run(["killall", "mpg123"])
                    mp3_file_path = None
                    current_track = None
                    time.sleep(2)
                
                elif id == IdTrack001:
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

                elif id == IdTrack003:
                    mp3_file_path = "/raspitracks/Track003.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack004:
                    mp3_file_path = "/raspitracks/Track004.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack005:
                    mp3_file_path = "/raspitracks/Track005.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack006:
                    mp3_file_path = "/raspitracks/Track006.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack007:
                    mp3_file_path = "/raspitracks/Track007.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack008:
                    mp3_file_path = "/raspitracks/Track008.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()
                    
                    current_track = mp3_file_path

                elif id == IdTrack009:
                    mp3_file_path = "/raspitracks/Track009.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack010:
                    mp3_file_path = "/raspitracks/Track010.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack011:
                    mp3_file_path = "/raspitracks/Track011.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack012:
                    mp3_file_path = "/raspitracks/Track012.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack013:
                    mp3_file_path = "/raspitracks/Track013.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack014:
                    mp3_file_path = "/raspitracks/Track014.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack015:
                    mp3_file_path = "/raspitracks/Track015.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack016:
                    mp3_file_path = "/raspitracks/Track016.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack016:
                    mp3_file_path = "/raspitracks/Track016.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack017:
                    mp3_file_path = "/raspitracks/Track017.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack018:
                    mp3_file_path = "/raspitracks/Track018.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack019:
                    mp3_file_path = "/raspitracks/Track019.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack020:
                    mp3_file_path = "/raspitracks/Track020.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack021:
                    mp3_file_path = "/raspitracks/Track021.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack022:
                    mp3_file_path = "/raspitracks/Track022.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack023:
                    mp3_file_path = "/raspitracks/Track023.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack024:
                    mp3_file_path = "/raspitracks/Track024.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack025:
                    mp3_file_path = "/raspitracks/Track025.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack026:
                    mp3_file_path = "/raspitracks/Track026.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack027:
                    mp3_file_path = "/raspitracks/Track027.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack028:
                    mp3_file_path = "/raspitracks/Track028.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack029:
                    mp3_file_path = "/raspitracks/Track029.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack030:
                    mp3_file_path = "/raspitracks/Track030.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack031:
                    mp3_file_path = "/raspitracks/Track031.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack032:
                    mp3_file_path = "/raspitracks/Track032.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack033:
                    mp3_file_path = "/raspitracks/Track033.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack034:
                    mp3_file_path = "/raspitracks/Track034.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack035:
                    mp3_file_path = "/raspitracks/Track035.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack036:
                    mp3_file_path = "/raspitracks/Track036.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack037:
                    mp3_file_path = "/raspitracks/Track037.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack038:
                    mp3_file_path = "/raspitracks/Track038.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack039:
                    mp3_file_path = "/raspitracks/Track039.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack040:
                    mp3_file_path = "/raspitracks/Track040.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack041:
                    mp3_file_path = "/raspitracks/Track041.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack042:
                    mp3_file_path = "/raspitracks/Track042.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack043:
                    mp3_file_path = "/raspitracks/Track043.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack044:
                    mp3_file_path = "/raspitracks/Track044.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack045:
                    mp3_file_path = "/raspitracks/Track045.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack046:
                    mp3_file_path = "/raspitracks/Track046.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack047:
                    mp3_file_path = "/raspitracks/Track047.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack048:
                    mp3_file_path = "/raspitracks/Track048.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack049:
                    mp3_file_path = "/raspitracks/Track049.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path

                elif id == IdTrack050:
                    mp3_file_path = "/raspitracks/Track050.mp3"

                    # stop the currently playing track, if any
                    if current_track is not None:
                        subprocess.run(["killall", "mpg123"])
                        current_track = None

                    # create a thread to play the song in the background
                    song_thread = threading.Thread(target=play_mp3, args=(mp3_file_path,))
                    song_thread.start()

                    current_track = mp3_file_path
                # continue adding as many "elifs" for songs/albums that you want to play
            
            #WENN der gleiche Chip aufgelegt ist wie zuvor UND der Player spielt: mach nix und check ob das noch so ist
            elif id == checkvar and is_mpg123_playing() is True:                            
                time.sleep(3)
                id = reader.read()[0]
            
            #WENN der gleiche Chip aufgelegt ist wie zuvor UND der Player NICHT spielt: gib die Wiedergabe für den gleichen RFID Tag wieder frei
            elif id == checkvar and is_mpg123_playing() is False:
                 checkvar = 0
            

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...verändert")
        GPIO.cleanup()


