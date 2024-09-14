import time
import os
import random
import board
import pwmio
import audioio
import audiocore
import audiobusio
from adafruit_debouncer import Button
from digitalio import DigitalInOut, Direction, Pull
import simpleio

# Needed for original Prop Maker board
POWER_PIN = board.D10
SWITCH_PIN = board.D9

print(">>> Dino Firmware 0.0.0")

print("Initializing hardware...")

print("Enabling propmaker power")
external_power = DigitalInOut(POWER_PIN)
external_power.direction = Direction.OUTPUT
external_power.value = True

print("Initializing audio")
audio = audioio.AudioOut(board.A0)     # Speaker
mode = 0                               # Initial mode = OFF

def play_wav(name, loop=False):
    try:
        # TODO: See if we can pre-load this for responsiveness
        wave_file = open(name, "rb")
        wave = audiocore.WaveFile(wave_file)
        audio.play(wave, loop=loop)
    except:
        return

print("Initializing trigger")
pin = DigitalInOut(SWITCH_PIN)
pin.direction = Direction.INPUT
pin.pull = Pull.UP
trigger = Button(pin, long_duration_ms = 1000)
trigger_state = False

print(">>> Hardware initialization complete!")

print(">>> Initializing software state")
mode = 0
print(">>> Software initialization complete!")

print(">>> Entering main event loop")
while True:
    trigger.update()
    # startup
    if mode == 0:
        print("Startup mode begins...")
        print(mode)
        print("Startup mode complete!")
        mode = 1
    # idle
    elif mode == 1:
        # Read trigger
        if trigger.pressed:
            #audio.stop()
            mode = 3 
        print("Exiting idle mode")
    # make a dino call
    elif mode == 3:
        print("Entering call mode...")
        print(mode)
        # If sound isn't playing, play dino call sound
        if not audio.playing:
            print("> Making dino call")
            # play a random call
            filename = "raptor{}.wav".format(random.randint(1,2))
            play_wav(filename, loop=False)
        if trigger.released:
          # return to idle
          mode = 1
        print("Exiting call mode")
