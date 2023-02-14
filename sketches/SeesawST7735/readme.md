# Macropad Seesaw Display

#### For this project you will require the following:
 * 1x Adafruit MacroPad RP2040 (other boards will require tweaks to code.py)
 * 1x Adafruit Seesaw ATTiny8x7 (uses UPDI programmer but with stock firmware)
 * 1x 1.8" 160x128 ST7735 TFT Display (pins marked as I2C but is actually SPI)
 * 1x 4-pin mini JST-SH StemmaQT Cable (connects to the side closest to VIN)

<!-- link to code.py -->

#### Software SPI through a microcontroller can be quite slow. It can instead run at 20MHz on the ATTiny8x7 itself...
#### Stock Firmware Arduino Library: https://github.com/adafruit/Adafruit_seesawPeripheral

#### More info on Seesaw in CircuitPython: https://github.com/adafruit/Adafruit_CircuitPython_seesaw
#### More info on Adafruit Seesaw ATTiny8x7: https://learn.adafruit.com/adafruit-attiny817-seesaw/circuitpython

![screenshot](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/media/IMG_6216.jpg)
![screenshot](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/media/Seesaw_ST7735.png)