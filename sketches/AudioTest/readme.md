```py
# Audio Test - TheMindVirus, Adafruit Industries
# This sketch plays a test tone through various speakers connected to the macropad rp2040.
# The built-in piezo is usually mono and a TRS headphone jack with linked grounds is on the StemmaQT port.

# https://docs.circuitpython.org/en/latest/shared-bindings/audiopwmio/index.html

import board, audiocore, audiopwmio, digitalio, array, math, time

TIME = time
VOLUME = 0.1

DIO = digitalio.DigitalInOut
SE = DIO(board.SPEAKER_ENABLE)
SE.switch_to_output(value = True)

RATE = 96000
SZ = RATE // 440
SINE = array.array("H", [0] * SZ)
for i in range(0, SZ):
    SINE[i] = int((math.sin(math.pi * 2 * i / SZ) * (2 ** 15) + (2 ** 15)) * VOLUME)
WAVE = audiocore.RawSample(SINE, sample_rate = RATE)

DAC = audiopwmio.PWMAudioOut(board.SPEAKER)
DAC.play(WAVE, loop = True)
TIME.sleep(1)
DAC.stop()
DAC.deinit()

JACK = audiopwmio.PWMAudioOut(left_channel = board.SDA, right_channel = board.SCL)
JACK.play(WAVE, loop = True)
TIME.sleep(1)
JACK.stop()
JACK.deinit()

JACK = audiopwmio.PWMAudioOut(board.SDA)
JACK.play(WAVE, loop = True)
TIME.sleep(1)
JACK.stop()
JACK.deinit()

JACK = audiopwmio.PWMAudioOut(board.SCL)
JACK.play(WAVE, loop = True)
TIME.sleep(1)
JACK.stop()
JACK.deinit()
```
