import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

print("Gib her!")

while True:
        id = reader.read()[0]
        print(id)
        time.sleep(0.5)
        