"""Very basic example script to inject a volume change event into Box Of Stops
   - this can be heard in the changing volume of the note
   - it can also be seen - look for the master volume changing in the browser interface
   See http://boxofstops.com/onlinehelp/Extras_script
"""
print("In extras")

import boxofstops
import mido
import time
import threading

device_name = 'Roland HP Series MIDI 1'
channel = 0
control = 70 # Assuming CC#70 is mapped to the master volume in the Registration

def play_loop():
    while (True):
        print("Note on...")
        boxofstops.midi_in_event(device_name,mido.Message('control_change', control=control, channel=channel, value=0))
        boxofstops.midi_in_event(device_name,mido.Message('note_on', note=60, channel=channel, velocity=80))
        for v in range(0, 100, 5):
            boxofstops.midi_in_event(device_name,mido.Message('control_change', control=control, channel=channel, value=v))
            time.sleep(0.05)
        for v in range(100, 0, -5):
            boxofstops.midi_in_event(device_name,mido.Message('control_change', control=control, channel=channel, value=v))
            time.sleep(0.05)
        print("Note off...")
        boxofstops.midi_in_event(device_name,mido.Message('note_off', note=60, channel=channel, velocity=80))
        time.sleep(1)

boxofstops.add_device_channel(device_name,channel)

thread = threading.Thread(target = play_loop, args = ())
thread.start()

print("Extras loaded")