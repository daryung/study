int redaled = 13;
int buleled = 12;
int buzzer = 11;
int sounddi = 10;
int soundan = A0;

void setup() {
  pinMode(redaled, OUTPUT);
  pinMode(buleled, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(sounddi, INPUT);
  pinMode(soundan, INPUT);
  Serial.begin(9600);


}

void loop() {
  int digitalVal = digitalRead(sounddi);   // 소리 감지 여부
  int analogVal = analogRead(soundan);     // 소리 크기 값

  Serial.print("Digital: ");
  Serial.print(digitalVal);
  Serial.print("  Analog: ");
  Serial.println(analogVal);

  // 디지털 출력 기준으로 LED/부저 제어
  if (digitalVal == HIGH && soundan >= 300 ) {
    digitalWrite(redaled, HIGH);
   
  }  if (digitalVal == HIGH && soundan < 300 ) {
    digitalWrite(buleled, HIGH);
  }
   else {
    digitalWrite(redaled, LOW);
    digitalWrite(buleled, LOW);
    
  }

  delay(100);


}
