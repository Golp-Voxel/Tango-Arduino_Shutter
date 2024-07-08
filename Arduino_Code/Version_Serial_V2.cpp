#include <Arduino.h>
#include <stdlib.h>
#include <stdlib.h>
#include <stdio.h>

const int pin = 13; // Change this to a PWM-capable pin you're using
const unsigned long timeOpen = 1 * 1000; // Time to keep the pin HIGH, in milliseconds
const unsigned long timeClose = 2 * 1000; // Time to keep the pin LOW, in milliseconds

unsigned long previousMillis = 0;
int pinState = LOW;
String input = "";

void do_stuf(String str)
{
  if (str== "Off") {
    pinState = LOW;
    analogWrite(pin, pinState);
    Serial.println("Off was executed");
  }
   else if (str == "On") {
    pinState = 255;
    analogWrite(pin, pinState);
    Serial.println("On was executed");
  }
};


void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(pin, OUTPUT);
  analogWrite(pin, pinState);
}

void loop() {
  // send data only when you receive data:
  if(Serial.available() > 0)
  {
     input = Serial.readStringUntil('\n');
  }
  if (input != NULL)
  {
    if (input == "help" || input =="h")
    {
      Serial.println("Type: | On | Off |");
    }  
    do_stuf(input);
    input="";
  }
  // Serial.print("Ola\n\r");
}