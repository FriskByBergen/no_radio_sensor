
/* sensor node code for the Frisk Luft project at www.friskby.no
   the code has been tested with DFRobot Romeo
*/

#include <DHT.h>

int measurePin = 5; //Connect dust sensor to Arduino A0 pin
int ledPower = 5;   //Connect 3 led driver pins of dust sensor to Arduino D5
int gaspin = 2; // A2

int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;

float voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;
float gasvalue = 0;

#define DHTPIN 2     // I/O pin of the DHT-22
#define DHTTYPE DHT22   // DHT 22  (AM2302)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(ledPower, OUTPUT);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // about every 10 seconds
  static unsigned long lastTime = millis();
  if (millis() - lastTime >= 10000)
  {
    lastTime = millis();
    digitalWrite(ledPower, LOW); // power on the LED
    delayMicroseconds(samplingTime);
    voMeasured = analogRead(measurePin); // read the dust value
    delayMicroseconds(deltaTime);
    digitalWrite(ledPower, HIGH); // turn the LED off
    delayMicroseconds(sleepTime);

    // read the gas sensor too
    gasvalue = analogRead(gaspin);
   
    // 0 - 5V mapped to 0 - 1023 integer values
    calcVoltage = voMeasured * (5.0 / 1023.0);
    int h = dht.readHumidity();
    int t = dht.readTemperature();
    int d = voMeasured;
    // check if returns are valid, if they are NaN (not a number) then something went wrong!
    Serial.print(voMeasured);
    Serial.print(" , ");
    Serial.print(t);
    Serial.print(" , ");
    Serial.print(h);
    Serial.print(" , ");
    Serial.println(gasvalue);
  }
}
