#Version 1.7
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import subprocess
import threading
import time

IdTrack001 = 128213821516
IdTrack002 = 815291214050
IdTrack003 = 881947158552
IdTrack004 = 58571794464
IdTrack005 = 1090169120930
IdTrack006 = 57330215129
IdTrack007 = 333449701472
IdTrack008 = 265552177253
IdTrack009 = 332208122009
IdTrack010 = 608327608480
IdTrack011 = 125312608430
IdTrack012 = 607086028889
IdTrack013 = 883205515488
IdTrack014 = 743937910804
IdTrack015 = 814754605198
IdTrack016 = 469949327495
IdTrack017 = 1018815817812
IdTrack018 = 1089632512206
IdTrack019 = 744827234375
IdTrack020 = 194198874261
IdTrack021 = 265015568393
IdTrack022 = 1019705141255
IdTrack023 = 469076781269
IdTrack024 = 539893475401
IdTrack025 = 195088197824
IdTrack026 = 266072664140
IdTrack027 = 196464060432
IdTrack028 = 950449055763
IdTrack029 = 540950571020
IdTrack030 = 471341967440
IdTrack031 = 125832112340
IdTrack032 = 815828478156
IdTrack033 = 746219874448
IdTrack034 = 400710019220
IdTrack035 = 1090706385036
IdTrack036 = 1021097781456
IdTrack037 = 675587926100
IdTrack038 = 468506814718
IdTrack039 = 1089330981083
IdTrack040 = 538635708556
IdTrack041 = 743384721470
IdTrack042 = 264714037272
IdTrack043 = 813513615436
IdTrack044 = 1018262628478
IdTrack045 = 539591944280
IdTrack046 = 608244312212
IdTrack047 = 57683257595
IdTrack048 = 262432270497
IdTrack049 = 883122219220
IdTrack050 = 332561164475
IdStop1 = 1063282416622
IdStop2 = 620020573937

def play_mp3(file_path):
    subprocess.run(["mpg123", file_path])

# Erstdefinition der Variable current_track
current_track = None

while True:
    try:
        reader = SimpleMFRC522()

        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Ich warte auf einen RFID-Scan")
            id = reader.read()[0]
            print("Du hast folgenden RFID-Tag gelesen:",id)
            
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

            elif id == IdStop1 or id == IdStop2:
                mp3_file_path = "/raspitracks/Track000.mp3"

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

