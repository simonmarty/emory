unsigned long A;
unsigned long B;
unsigned long sharedPrime = 23;
unsigned long sharedBase = 5;

unsigned long bobSecret = 7;
unsigned long sharedSecret;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);   
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()) {
    A = Serial.parseInt();
    delay(30);
    if(A != 0) {
      B = Pow(sharedBase, bobSecret) % sharedPrime;
      Serial.println(B);
      sharedSecret = Pow(A, bobSecret) % sharedPrime;      
    }
  }
}

unsigned long Pow(unsigned long base, unsigned long ex) {
  unsigned long res = 1;
  for(unsigned long i = 0; i < ex; i++) {
    res *= base;
  }
  return res;
}
