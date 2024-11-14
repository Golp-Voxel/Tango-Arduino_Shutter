#include <Arduino.h>
#include <stdlib.h>
#include <stdlib.h>
#include <stdio.h>
#include <ArduinoJson.h>

const int pin = 13; // Change this to a PWM-capable pin you're using
const unsigned long timeOpen = 1 * 1000; // Time to keep the pin HIGH, in milliseconds
const unsigned long timeClose = 2 * 1000; // Time to keep the pin LOW, in milliseconds

unsigned long previousMillis = 0;
int pinState = LOW;
String input = "";

String main_key_1 = "action";
String main_key_2 = "operation";
unsigned long time_ms = 1;
int ciclos = 1;
bool text_out = true;

void do_stuf(String str)
{
  if (str== "Off") {
    pinState = LOW;
    analogWrite(pin, pinState);
    if (text_out)
      Serial.println("Off was executed");
  }
   else if (str == "On") {
    pinState = 255;
    analogWrite(pin, pinState);
    if (text_out)
      Serial.println("On was executed");
  }
};

void ciclo_run()
{
  for (int i = 0; i< ciclos;i++)
  {
    Serial.println("Cicle is going to be executed");
    text_out = false;
    do_stuf("On");
    delay(time_ms);
    do_stuf("Off");
    delay(50);
  }
}


void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(pin, OUTPUT);
  analogWrite(pin, pinState);
};

void brain(JsonDocument& doc_rec)
{
  if (doc_rec.containsKey(main_key_1) )
  {
      text_out = true;
      String status = doc_rec[main_key_1];
      do_stuf(status);
  }
  else if (doc_rec.containsKey(main_key_2) )
  {
    time_ms = (int)doc_rec[main_key_2]["time_ms"];
    ciclos = (int)doc_rec[main_key_2]["cicles"];
    ciclo_run();
  }
};



void loop() {
  unsigned long currentMillis = millis();
  StaticJsonDocument<500> doc_rec;
  // send data only when you receive data:
  if (Serial.available() > 0) {
    deserializeJson(doc_rec, Serial);
    brain(doc_rec);
  }
 
}