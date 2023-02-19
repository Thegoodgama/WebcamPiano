#include <cvzone.h>
SerialData serialData(1,1);

int valRec[1];
void setup() {
  // put your setup code here, to run once:
  serialData.begin();
  pinMode(13,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
}

void loop() {
  serialData.Get(valRec);
  if(valRec[0] == 1){
    digitalWrite(9,HIGH);
    tone(13, 523, 2000); //C
    delay(750);
    noTone(13);
    digitalWrite(9,LOW);
    

 }
  else if(valRec[0] == 2){
    digitalWrite(10,HIGH);
    tone(13, 587, 2000); //D
    delay(750);
    noTone(13);
    digitalWrite(10,LOW);
  
 }
  else if(valRec[0] == 3){
    digitalWrite(11,HIGH);
    tone(13, 659, 2000); //E
    delay(750);
    noTone(13);
     digitalWrite(11,LOW);
    
 }
   else if(valRec[0] == 4){
     digitalWrite(12,HIGH);
    tone(13, 784, 2000); //G
    delay(750);
    noTone(13);
     digitalWrite(12,LOW);
   
 }
 else if (valRec[0] == 5)
 noTone(13);

 delay(10);
 
}
