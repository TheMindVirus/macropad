# macropad

Adafruit Macropad RP2040 with Transparent Lego Keycaps and Sounds from The Crystal Maze

# Introduction
The Macropad by Adafruit Industries is a Shortcut Keyboard powered by a Raspberry Pi RP2040. \
The same microcontroller powers the Raspberry Pi Pico RP2040 and the usage is much the same.

There are a wide range of CherryMX keyboard switches to choose from, each with different \
tactile feel and clickyness. How do you know which keys you like before buying a whole keyboard? \
This project will see you assembling your own Macropad with a selection of different CherryMX keys \
and keycaps to find what fits your preference and needs.

# Prototype
It is a good idea to prototype in any way you like before you receive the budget for your project. \
It's also useful for showing people what you want to create so that they know how to help you. \
I decided to create my prototype in Unity3D using Unity WebGL Player so it can run on a phone.

Demo: https://themindvirus.github.io/macropad/

![Prototype.png](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/Prototype.png)

# Parts
To start with, I purchased a fine selection of Glorious CherryMX Switches from OverclockersUK. \
Every key switch in the sample pack is a different flavour of tactile feel and clickyness. \
You will need at least 12 of them to complete your Macropad. (More info in `./costings.txt`)

![IMG_4910.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4910.JPG)

To source the custom Lego pieces and also to create the original prototype, I turned to BrickLink Studio. \
The Studio 2.0 Software is much like Lego Digital Designer before it and allows you to freely make design choices. \
The prototype uses 2x2 Tiles whereas I ended up using 2x2 Bricks and 1x1 Tiles for the final build.

![IMG_4911.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4911.JPG)

This wouldn't be a project about the Adafruit Macropad RP2040 without an Adafruit Macropad RP2040. \
I chose the one which doesn't come with any keys or backplate because I wanted to customise it and \
still be able to see the RP2040 that's powering the board on the underside.

![IMG_4912.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4912.JPG)

Here is a close-up of the back of the printed circuit board (PCB). The central chip with the Raspberry \
logo is the RP2040 that runs your custom programs. Beside it is some flash memory and a ribbon cable \
for the display. A small speaker plays tones of a frequency you specify in either Arduino or CircuitPython.

![IMG_4923.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4923.JPG)

The CherryMX keys are colour-coded to help identify their characteristics. The footprint of the Macropad \
allows you to choose between Cherry, Kailh and Gateron. Some switches are weighted differently from others \
and some emit a specific texture of sound when typed on repeatedly. There are also many more switch manufacturers.

![IMG_4924.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4924.JPG)

The key switches are modular and so are the keycaps, allowing for a huge range of possible combinations. \
Along with the Lego keycaps, I also purchased an assortment of Black Pudding keycaps from Adafruit. \
The underside of the keys will be lit with GRB NeoPixel Light Emitting Diodes (LEDs) so choose wisely.

![IMG_4931.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4931.JPG)

A single lead is all that is required to power the device, upload firmware to it and receive key data from it. \
The back of the Macropad has a USB Type-C connector for all of these purposes. The same reversible cable is used \
by chargers for mobile phones and a growing ecosystem of accessories, making it somewhat ubiquitous.

![IMG_4933.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4933.JPG)

If however your PC doesn't have a USB Type-C port available or within a cable's length, you may instead opt for \
a shorter USB Type-A to Type-C adapter cable, such as the one pictured below. This is ideal if you have a USB Hub \
on your desk. I will be using this cable with the USB Hub on the back of the Raspberry Pi Official Keyboard. 

![IMG_4935.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4935.JPG)

While attempting to attach the Lego keycaps to the CherryMX switches, I realised that this was not enough to hold \
the keycaps sturdily in place. The key switches came with a set of rubber inserts that fit around the axle on the \
top of each switch (some of which have square boundaries around them). I instead opted for some Blu Tack!

![IMG_4938.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4938.JPG)

# Assembly
Carefully, without applying too much pressure, align and attach each CherryMX switch to its slot on the Macropad. \
The pins are quite fragile and are prone to bending. They need to connect to the board's conductive contacts. \
No soldering is required; the switches should click into place. I also found a knob cap from an old defunct mixer.

![IMG_4939.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4939.JPG)

If you're using keycaps that are designed to fit on top of CherryMX switches then you may skip this step. \
For Lego keycaps you will need to apply a small blob of Blu Tack to the top of each switch axle before \
gently aligning and attaching each keycap. You're looking for it to hold strongly but not be too obtrusive.

![IMG_4942.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4942.JPG)

When you have attached your keycaps your Macropad should look something like this. The studs on top of \
the Lego bricks can give a unique feel to your shortcut keyboard, but some may prefer flatter keycaps. \
In this case, it is ideal to attach tiles on top of the studs before attaching the keycaps to their switches.

![IMG_4948.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4948.JPG)

This is what the finished Macropad should look like after attaching all the keycaps each with 4 tiles. \
You may have spare key switches and keycaps which can be swapped in and out as and when you wish. \
The next stage is to connect the Macropad to your PC and upload your own custom programs to it.

![IMG_4949.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4949.JPG)

As soon as you plug in your Adafruit Macropad produced by DigiKey Electronics, you will see their logos \
flash briefly on the display and all your keys will illuminate with a sequence of breathing light colours. \
This is the demo program and it gets overwritten by your code. (See `./Factory Firmware/` for similar code)

![IMG_4955.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4955.JPG)

You can use either Arduino IDE or CircuitPython to program your Macropad. The versions used in this project \
were Arduino IDE 1.8.13 and CircuitPython7-rc1. You will also need to install the relevant Macropad Libraries. \
Uploading firmware is the same process as for the Raspberry Pi Pico. Press in the Rotary Encoder for BOOTSEL.

![IMG_4958.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4958.JPG)

When you hold down BOOTSEL while powering on your Macropad, it will appear as a USB Flash Drive, \
but it is only for storing temporary programs (not for important documents which may be lost). \
Dragging `./CircuitPython7.uf2` to this drive will cause it to disappear as "RPI-RP2" and reappear as "CIRCUITPY".

![IMG_4960.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4960.JPG)

The Macropad requires no extra driver installation to work because it uses the USB Mass Storage Standard Class \
which is built into many operating systems. My sketch turns the keys into the hidden F13-F24 keys on Windows \
and makes a sound on each key press. If however you want to do something different then feel free to experiment.

![IMG_4962.JPG](https://github.com/TheMindVirus/macropad/blob/main/Visual%20Assets/IMG_4962.JPG)

I hope you enjoyed following my project and maybe even have your own Macropad designs and sketches as a result. \
If you like what you see, please consider clicking the sponsor button at the top of this page while perusing. \
More content is being created every day by a diverse group of people who are sometimes unappreciated for their work.

# Useful Links
Home: https://github.com/TheMindVirus/macropad/ \
Demo: https://themindvirus.github.io/macropad/ \
RP2040: https://www.raspberrypi.org/products/raspberry-pi-pico/ \
Macropad: https://learn.adafruit.com/adafruit-macropad-rp2040?view=all \
CircuitPython: https://circuitpython.org/
CherryMX: https://www.cherrymx.de/en \
BrickLink: https://www.bricklink.com/v3/studio/download.page \
Lego Digital Designer: https://www.lego.com/en-us/ldd \
Unity: https://unity.com/
