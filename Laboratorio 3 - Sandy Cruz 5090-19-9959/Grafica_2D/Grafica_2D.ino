#include "Potenciometro.h"

Encender_LED encender_led;

void setup() {
  Serial.begin(9600);
  encender_led.setU(13);
}

void loop() {
  encender_led.encender(13);
}
