
 

/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial



#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "16MKL22H8_Wa-WFznE3yvJcFyWj88buT";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "Abhishek";
char pass[] = "Madmax2001";

void setup()
{
  // Debug console
  Serial.begin(9600);

  Blynk.begin(auth, ssid, pass);
  // You can also specify server:
  //Blynk.begin(auth, ssid, pass, "blynk-cloud.com", 80);
  //Blynk.begin(auth, ssid, pass, IPAddress(192,168,1,100), 8080);
}

void loop()
{ 
  Blynk.run();
}
