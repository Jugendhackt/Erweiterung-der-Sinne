/***************************************************************************
  This is a library for the BME280 humidity, temperature & pressure sensor

  Designed specifically to work with the Adafruit BME280 Breakout
  ----> http://www.adafruit.com/products/2650

  These sensors use I2C or SPI to communicate, 2 or 4 pins are required
  to interface.

  Adafruit invests time and resources providing this open source code,
  please support Adafruit andopen-source hardware by purchasing products
  from Adafruit!

  Written by Limor Fried & Kevin Townsend for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ***************************************************************************/

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)

//Adafruit_BME280 bme; // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO,  BME_SCK);

int gasSensorAPin = 0;

int gasSensorVal = 0;


const int buzzerPin = 4; //buzzer to arduino pin 9
const int maxGasAmount = 200;
void setup() {
  Serial.begin(9600);
  Serial.println(F("BME280 test"));

  if (!bme.begin()) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
    gasSensorVal = analogRead(gasSensorAPin);
    Serial.print("temp:");
    Serial.print(bme.readTemperature());
    Serial.print(",");

    Serial.print("hPa:");
    Serial.print(bme.readPressure() / 100.0F);
    Serial.print(",");

    Serial.print("altitude:");
    Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
    Serial.print(",");

    Serial.print("humidity:");
    Serial.print(bme.readHumidity());
    Serial.print(",");

    Serial.print("gassensor:");
    Serial.print(gasSensorVal);

    if(gasSensorVal > maxGasAmount){
        tone(buzzerPin, gasSensorVal*3);
    } else{
        noTone(buzzerPin);
    }
    Serial.println();
    delay(100);
}
