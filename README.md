# dino-firmware

Simple firmware for the original [Adafruit Propmaker Feather](https://learn.adafruit.com/adafruit-prop-maker-featherwing/overview) to make raptor sounds for a Halloween project.

# TODO
Battery charge could be reflected by playing a "I'm hungry" sound.  This [Adafruit](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/power-management#measuring-battery-3122383) section goes into the details, but the code to measure battery charge looks like this:

```
import board
from analogio import AnalogIn

vbat_voltage = AnalogIn(board.VOLTAGE_MONITOR)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2


battery_voltage = get_voltage(vbat_voltage)
print("VBat voltage: {:.2f}".format(battery_voltage))
```

(the hard part is finding an appropriate sound...)

# References
* https://learn.adafruit.com/adafruit-prop-maker-featherwing/overview
* https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51
* https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/power-management#measuring-battery-3122383
* https://learn.adafruit.com/circuitpython-safe-mode/safe-mode-reasons
* https://soundbible.com/1372-Raptor-Call.html
* https://docs.micropython.org/en/latest/library/random.html
* https://www.fredscave.com/35-micropython-formatting-strings.html
* https://learn.adafruit.com/welcome-to-circuitpython/the-repl
