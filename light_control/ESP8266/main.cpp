#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "NumeleWiFi";
const char* password = "ParolaWiFi";

const char* serverUrl = "http://adresa_serverului:5000/api/bedroom_light";  // Endpoint-ul API

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectare la WiFi...");
  }
  Serial.println("Conectat la WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    int httpCode = http.GET();

    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println(payload);

      // Parsează răspunsul JSON
      StaticJsonDocument<200> doc;
      deserializeJson(doc, payload);
      bool state = doc["state"];
      String color = doc["color"];

      // Controlează LED-ul sau releul
      digitalWrite(D1, state ? HIGH : LOW);  // D1 poate fi schimbat cu pinul folosit pentru control
      // Adaugă logica pentru a seta culoarea, dacă este necesar
    } else {
      Serial.println("Eroare la conectare");
    }

    http.end();
  }

  delay(10000);  // Așteaptă 10 secunde înainte de a verifica din nou
}
