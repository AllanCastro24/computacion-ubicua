/****************************************
   Include Libraries
 ****************************************/
#include "UbidotsEsp32Mqtt.h"

/****************************************
   Definir constantes
 ****************************************/
const char *UBIDOTS_TOKEN = "BBFF-uiHDZ3oCZ7DAUMcuvpiFawSga4keUW";  // Ubidots TOKEN
const char *WIFI_SSID = "POCOX3";      //Wi-Fi SSID
const char *WIFI_PASS = "allan123";      //Wi-Fi password
const char *DEVICE_LABEL = "esp32";   // ID Device
const char *VARIABLE_LABEL = "foco"; // ID Variable

const uint8_t LED = 2; // Pin usado

Ubidots ubidots(UBIDOTS_TOKEN);

void callback(char *topic, byte *payload, unsigned int length)
{
  Serial.print("Mensaje recibido [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++)
  {
    Serial.print((char)payload[i]);
    if ((char)payload[0] == '1')
    {
      digitalWrite(LED, HIGH);
    }
    else
    {
      digitalWrite(LED, LOW);
    }
  }
  Serial.println();
}

/****************************************
   Main Functions
 ****************************************/

void setup()
{
  Serial.begin(115200);
  pinMode(LED, OUTPUT);

  ubidots.connectToWifi(WIFI_SSID, WIFI_PASS);
  ubidots.setCallback(callback);
  ubidots.setup();
  ubidots.reconnect();
  ubidots.subscribeLastValue(DEVICE_LABEL, VARIABLE_LABEL);
}

void loop()
{
  if (!ubidots.connected())
  {
    ubidots.reconnect();
    Serial.println("Tratando de conectar");
    ubidots.subscribeLastValue(DEVICE_LABEL, VARIABLE_LABEL);
  }
  ubidots.loop();
}