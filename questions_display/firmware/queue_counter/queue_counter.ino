#include <SoftwareSerial.h>


String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

SoftwareSerial led1(4, 5);
SoftwareSerial led2(10, 11);



void setup() {
  // initialize serial:
  Serial.begin(9600);
  Serial.println("Ola mundo!");
  
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  
  led1.begin(9600);
  led2.begin(9600);
  
  led1.print((char)0x76);
  led1.print("1234");
  led2.print((char)0x76);
  led2.print("5678");


  pinMode(3, OUTPUT);
  analogWrite(3, 0);
  
}

void loop() {

  // print the string when a newline arrives:
  if (stringComplete) {
    
    analogWrite(3, map(inputString.substring(10, 14).toInt(), 0, 100, 0, 255));

    //Serial.println(inputString);
    //Serial.println(inputString.substring(0, 4));
    //Serial.println(inputString.substring(5, 9));
    //Serial.println(inputString.substring(10, 14));
    
    led1.print((char)0x76);
    led1.print(inputString.substring(0, 4));
    
    led2.print((char)0x76);
    led2.print(inputString.substring(5, 9));

    
    Serial.print("OK "); 
    Serial.println(inputString); 

    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}


/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}


