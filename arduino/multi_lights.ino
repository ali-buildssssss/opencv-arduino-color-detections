
const int red=8;
const int yellow=9;
const int blue=10;

void setup(){
  pinMode(red,OUTPUT);
  Serial.begin(9600);
  Serial.println("serial communication start");

}

void loop(){
  if (Serial.available()>0){
    char command=Serial.read();



    if (command=='r'){
      digitalWrite(red,HIGH);
      digitalWrite(yellow,LOW);
      digitalWrite(blue,LOW);
      Serial.println("red led on");
    }
    else if (command=='b'){
      digitalWrite(blue,HIGH);
      digitalWrite(yellow,LOW);
      digitalWrite(red,LOW);
      Serial.println("blue led on");
    }
    else if (command=='y'){
      digitalWrite(yellow,HIGH);
      digitalWrite(blue,LOW);
      digitalWrite(red,LOW);
      Serial.println("yellow led on");
    }
    else if(command=='0'){
      digitalWrite(yellow,LOW);
      digitalWrite(blue,LOW);
      digitalWrite(red,LOW);
      Serial.println("all led of");

    }
  }
}
