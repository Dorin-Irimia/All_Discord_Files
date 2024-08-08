#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "numele_tua_wi-fi";
const char* password = "parola_ta_wi-fi";

// Definirea pinii GPIO unde sunt conectate becurile
#define OWL_PIN 5  // GPIO 5 (D1 pe NodeMCU)
#define BEDROOM_PIN 4  // GPIO 4 (D2 pe NodeMCU)

ESP8266WebServer server(80);

void setup() {
  // Inițializarea serială pentru debugging
  Serial.begin(115200);

  // Conectare la Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Conectare la Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Conectat! IP Address: ");
  Serial.println(WiFi.localIP());

  // Configurarea pinilor ca OUTPUT
  pinMode(OWL_PIN, OUTPUT);
  pinMode(BEDROOM_PIN, OUTPUT);

  // Setarea stării inițiale (oprit)
  digitalWrite(OWL_PIN, LOW);
  digitalWrite(BEDROOM_PIN, LOW);

  // Rute API
  server.on("/owl/on", HTTP_GET, []() {
    digitalWrite(OWL_PIN, HIGH);
    server.send(200, "text/plain", "Owl light is ON");
  });

  server.on("/owl/off", HTTP_GET, []() {
    digitalWrite(OWL_PIN, LOW);
    server.send(200, "text/plain", "Owl light is OFF");
  });

  server.on("/bedroom/on", HTTP_GET, []() {
    digitalWrite(BEDROOM_PIN, HIGH);
    server.send(200, "text/plain", "Bedroom light is ON");
  });

  server.on("/bedroom/off", HTTP_GET, []() {
    digitalWrite(BEDROOM_PIN, LOW);
    server.send(200, "text/plain", "Bedroom light is OFF");
  });

  // Pornirea serverului
  server.begin();
  Serial.println("Serverul web a pornit!");
}

void loop() {
  // Serverul rulează
  server.handleClient();
}
