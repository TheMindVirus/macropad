#include <Adafruit_SH110X.h>
#include <Adafruit_NeoPixel.h>
#include <RotaryEncoder.h>
#include <Wire.h>

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUM_NEOPIXEL, PIN_NEOPIXEL, NEO_GRB + NEO_KHZ800);
Adafruit_SH1106G display = Adafruit_SH1106G(128, 64, &SPI1, OLED_DC, OLED_RST, OLED_CS);
RotaryEncoder encoder(PIN_ROTA, PIN_ROTB, RotaryEncoder::LatchMode::FOUR3);

uint8_t j = 0;
bool i2c_found[128] = {false};
int encoder_pos = 0;
void checkPosition() { encoder.tick(); }

void setup()
{
    Serial.begin(115200);
    delay(100);
    Serial.println("Adafruit Macropad with RP2040");

    pinMode(PIN_SPEAKER, OUTPUT);
    digitalWrite(PIN_SPEAKER, LOW);
    tone(PIN_SPEAKER, 988, 100);
    delay(100);
    tone(PIN_SPEAKER, 1319, 200);
    delay(200);

    for (size_t i = 0; i < NUM_NEOPIXEL; ++i)
    {
        pinMode(i, INPUT_PULLUP);
    }
    pixels.begin();
    pixels.setBrightness(255);
    pixels.show();

    pinMode(PIN_ROTA, INPUT_PULLUP);
    pinMode(PIN_ROTB, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(PIN_ROTA), checkPosition, CHANGE);
    attachInterrupt(digitalPinToInterrupt(PIN_ROTB), checkPosition, CHANGE);  

    display.begin(0, true);
    display.display();
    display.setTextSize(1);
    display.setTextWrap(false);
    display.setTextColor(SH110X_WHITE, SH110X_BLACK);
    delay(1000);

    Wire.begin();
}

void loop()
{
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println("* Adafruit Macropad *");
  
    encoder.tick();
    int newPos = encoder.getPosition();
    if (encoder_pos != newPos)
    {
        Serial.print("Encoder:");
        Serial.print(newPos);
        Serial.print(" Direction:");
        Serial.println((int)(encoder.getDirection()));
        encoder_pos = newPos;
    }
    display.setCursor(0, 8);
    display.print("Rotary encoder: ");
    display.print(encoder_pos);
    
    if ((j & 0x3F) == 0)
    {
        Serial.println("Scanning I2C: ");
        Serial.print("Found I2C address 0x");
        for (size_t address = 0; address <= 0x7F; ++address)
        {
            Wire.beginTransmission(address);
            i2c_found[address] = (Wire.endTransmission() == 0);
            if (i2c_found[address])
            {
                Serial.print("0x");
                Serial.print(address, HEX);
                Serial.print(", ");
            }
        }
        Serial.println();
    }
  
    display.setCursor(0, 16);
    display.print("I2C Scan: ");
    for (size_t address = 0; address <= 0x7F; ++address)
    {
        if (!i2c_found[address]) { continue; }
        display.print("0x");
        display.print(address, HEX);
        display.print(" ");
    }
  
    display.setCursor(0, 24);
    if (!digitalRead(PIN_SWITCH))
    {
        Serial.println("Encoder button");
        display.print("Encoder pressed ");
        pixels.setBrightness(255);
    }
    else { pixels.setBrightness(80); }

    for (size_t i = 0; i < NUM_NEOPIXEL; ++i)
    {
        pixels.setPixelColor(i, Wheel(((i * 256 / NUM_NEOPIXEL) + j) & 255));
    }
  
    for (size_t i = 1; i <= NUM_NEOPIXEL; ++i)
    {
        if (!digitalRead(i))
        {
            Serial.print("Switch "); Serial.println(i);
            pixels.setPixelColor(i - 1, 0xFFFFFF);
            display.setCursor(((i - 1) % 3) * 48, 32 + (((i - 1) / 3) * 8));
            display.print("KEY");
            display.print(i);
        }
    }

    pixels.show();
    display.display();
    ++j;
}

uint32_t Wheel(byte WheelPos)
{
    if (WheelPos < 85) { return pixels.Color(255 - (WheelPos * 3), 0, (WheelPos * 3)); }
    else if (WheelPos < 170) { WheelPos -= 85; return pixels.Color(0, WheelPos * 3, 255 - (WheelPos * 3)); }
    else { WheelPos -= 170; return pixels.Color((WheelPos * 3), 255 - (WheelPos * 3), 0); }
}
