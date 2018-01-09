"""Very basic example script to inject a note from a known device name into Box Of Stops
   See http://boxofstops.com/onlinehelp/Extras_script
"""
print("In extras")

import boxofstops
import mido
import time
import threading

device_name = 'Roland HP Series MIDI 1'
channel = 0

def play_loop():
    while (True):
        print("Note on...")
        boxofstops.midi_in_event(device_name,mido.Message('note_on', note=60, channel=channel, velocity=80))
        time.sleep(1)
        print("Note off...")
        boxofstops.midi_in_event(device_name,mido.Message('note_off', note=60, channel=channel, velocity=80))
        time.sleep(1)

boxofstops.add_device_channel(device_name,channel)

thread = threading.Thread(target = play_loop, args = ())
thread.start()

print("Extras loaded")