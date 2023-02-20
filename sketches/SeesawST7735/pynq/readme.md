# PYNQ-Z2 Zynq7000 ST7735 Development Kit

PYNQ-Z2 is a Xilinx Zynq7000 FPGA Development Board from TUL/Digilent. \
It contains programmable MicroBlaze I/O units for simulating various processors.

![IMG_6239](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/IMG_6239.jpg)

The ST7735 Display has been ported to the board in its early stages. \
The Raspberry Pi Mailbox MicroBlaze was especially tricky to implement.

![IMG_6245](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/IMG_6245.jpg)

Xilinx and Digilent also manufacture a wide range of PMOD FPGA Peripheral Breakouts \
alongside TUL, WaveShare for the Spartan series and ALINX for the UltraScale cards.

![IMG_6246](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/IMG_6246.jpg)

The board runs Python on its own distribution of Linux that runs on underlying hardware \
which allows it to change its logical wiring bitstream on the fly to emulate different processors.

![PYNQ_docs](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/pynq_docs.png)

It is self documenting in that it can be configured with a Samba Network File Share \
much like common Network Attached Storage (NAS) for storing programs, images and schematics.

![pynq_gpio_read](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/pynq_gpio_read.png)

While the stock firmware shipped running Jupyter Notebook Server, this ran into problems \
so I installed a custom build of Node-RED which can interface with the board via Linux commands.

![node_red](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/node_red.png)

The Zynq Adaptive SoC has been implemented in various professional grade industrial goods \
such as the compute card that drives multi-channel networked audio in the Focusrite RedNet 5 Rack.

![focusrite](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/focusrite.png)

The compute card in question is the Audinate Dante Brooklyn 2, which has been recently updated \
from using a Xilinx Spartan to using a Zynq Adaptive SoC, similar to the design of the PYNQ-Z2.

![brooklyn3](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/brooklyn3.png)

Since then, Xilinx has been bought by AMD and all the chips have undergone a rebrand, along with \
the red development boards which AMD once used in their ascension labs to bring up AMD processors.

![AMDzynq](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SeesawST7735/pynq/AMDzynq.png)

AMD Xilinx at ARM Tech Conference 2014: https://youtu.be/pcB-AXA_DIQ?t=1506
AMD at CES 2023: https://www.youtube.com/live/OMxU4BDIm4M?feature=share&t=3892
