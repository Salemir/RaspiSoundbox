import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
reader = SimpleMFRC522()

while True:
        print("Gib her!")
        id = reader.read()[0]
        print(id)
        time.sleep(0.5)