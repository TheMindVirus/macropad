#include <Wire.h>

//For StemmaQT Cable, SDA and SCL pinswapped on Uno Rev3
//Connect Yellow to SCL and Green to SDA
//Alternatively connect Yellow to A5 and Green to A4
//Hardware I2C would require automatic pinswap detection

void setup()
{
    Wire.begin(0x08);
    Wire.onRequest(Wire_onRequest);
    Wire.onReceive(Wire_onReceive);
    Serial.begin(115200);
}

void loop()
{
    Wire.write("Something");
    delay(1000);
}

void Wire_onRequest(int address)
{
    Serial.println(address);
    Wire.write("Nothing");
}

void Wire_onReceive(int address)
{
    Serial.println(address);
    while (Wire.available() > 0) { Serial.print((char)Wire.read()); }
    Serial.println();
}
