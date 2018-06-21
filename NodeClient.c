#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
     
const char* ssid     = "AP";
const char* password = "10203040";     
int port = 555;
char * ip = "192.168.43.161";

WiFiUDP udp;
char * data = "v";

int sensorPin = D2;

int myvalue = 0;
int readedValue = 0;

int wifiStatus;

void setup() {

    pinMode(sensorPin, INPUT);
    pinMode(D4, OUTPUT);

    // 1 = Disable, 0 = Enable
    digitalWrite(D4, 1);

    Serial.begin(115200);
    delay(200);

    // We start by connecting to a WiFi network
    Serial.println();
    Serial.println();
    Serial.print("Your are connecting to; ");
    Serial.println(ssid);

    WiFi.mode(WIFI_STA);
    udp.begin(port);
}   
     
void loop() {

    do_sensor();
    do_connect();
    do_send();
    do_listen();

    Serial.println("");
    Serial.print("My value: ");
    Serial.println(myvalue);
    Serial.print("Status value: ");
    Serial.println(readedValue);

    switch (data[0]) {
    
        case '%':
          digitalWrite(D4, HIGH);
          delay(2000);
          break;
          
        case 'm':
          digitalWrite(D4, LOW);
          delay(2000);
          break;
          
        case 's':
          digitalWrite(D4, LOW);
          delay(250);
          digitalWrite(D4, HIGH);
          delay(250);
          digitalWrite(D4, LOW);
          delay(250);
          digitalWrite(D4, HIGH);
          delay(250);
          digitalWrite(D4, LOW);
          delay(250);
          digitalWrite(D4, HIGH);
          delay(250);
          digitalWrite(D4, LOW);
          delay(250);
          digitalWrite(D4, HIGH);
          delay(250);
          digitalWrite(D4, LOW);
          delay(250);
          digitalWrite(D4, HIGH);
          break;
      
    }
}

void do_sensor() 
{
    myvalue = analogRead(A0);
}

void do_connect() {

    wifiStatus = WiFi.status();

    if(wifiStatus == WL_CONNECTED) {
         
        Serial.println("Your IP address is: ");
        Serial.println(WiFi.localIP());  

        delay(100);
    }
    else {
        Serial.println("");
        Serial.println("WiFi not connected, trying again ...");
        WiFi.begin(ssid, password);
        delay(1000);
    }

    delay(1000);
}

void do_send() {

    if (wifiStatus == WL_CONNECTED) {

        udp.beginPacket(ip, port);
        udp.println(myvalue);
        udp.endPacket();

        Serial.print("Sending: ");
        Serial.println(myvalue);

        delay(5);
    }
    else {
        Serial.println("Connection failed");
        delay(150);
    }

}

void do_listen() {

    if (udp.parsePacket() > 0)
    {
        data = "";

        while (udp.available() > 0)
        {
            char z = udp.read();
            data += z;
        }

        Serial.println("");
        Serial.print("Received data: ");
        Serial.println(data);
    }
}
