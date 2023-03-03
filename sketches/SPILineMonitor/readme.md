# SPI Line Monitor

![screenshot](https://github.com/TheMindVirus/macropad/blob/archive/sketches/SPILineMonitor/IMG_6283.jpg)

```c
#include <SPI.h>

//Standard SPI Pins Plus
#define GND   GND //Pi GND
#define CS    9  //Pi CE1
//MOSI and MISO may also be pinswapped

static int i = 0;

void setup()
{
    Serial.begin(115200);
    SPI.begin();
    pinMode(SS, INPUT); //Required for Read?
    pinMode(CS, INPUT);
    pinMode(A0, INPUT);
    pinMode(A1, OUTPUT);
    pinMode(12, OUTPUT); //This was missing...
}

void loop()
{
i = SPI.transfer(0x1F);
    Serial.println(i, HEX);
    digitalWrite(A1, digitalRead(A0));
}
```