#VolumeControl 1.1
import RPi.GPIO as GPIO
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

# Set the initial volume
set_volume(volume)

# Wait for button presses
while True:
    pass

# Clean up GPIO pins when the script is stopped
GPIO.cleanup()
