#!/usr/bin/python3

from gpiozero import Button
from signal import pause
from os import system
from os import environ

environ['HASS_SERVER']="http://homeassistant:8123"
# see https://www.home-assistant.io/docs/authentication/
environ['HASS_TOKEN']="put your key here"

pins = [19, 26, 21, 20, 16]

buttons = [Button(pin, bounce_time=0.05) for pin in pins]

def button_callback(button):
    if button.pin.number not in pins:
        # How did we get here?
        return

    swtich_number = pins.index(button.pin.number)

    print("Pressed Button {}".format(swtich_number))
    system("hass-cli service call automation.trigger --arguments entity_id=automation.olkb_terminal_button_{}".format(swtich_number))

for button in buttons:
    button.when_pressed = button_callback

pause()

