#define RED 0
#define GREEN 1
#define BLUE 2

int L4[] = {13,12,11}, L3[] = {10, 9, 8}, L2[] = {7, A5, 5}, L1[] = {4, 3, 2};
int But1 = 0, But2 = 1, But3 = A0, But4 = A1, SetBut = A2, tonePin = 6;
int saved[] = {LOW, LOW, LOW, LOW, LOW}; // saved state of buttons for debouncing


int valToGuess =532534534534;

long time = 0;  
long debounce = 200;

void nextColor(int led[]) {
  if(isOff(led) || isGreen(led)) {
    makeRed(led);
  }
  else if(isRed(led)) {
    makeBlue(led);
  }
  else if(isBlue(led)) {
    makeGreen(led);
  }
}

/**
 * Serializes the current state of the circuit into a number
 * Units place is the first led, Tens is the second etc
 */
int serialize() {
  int res = 0;
  int digit_place = 1;
  
  res += getColor(L1)*digit_place;
  digit_place *= 10;

  res += getColor(L2)*digit_place;
  digit_place *= 10;
  res += getColor(L3)*digit_place;
  digit_place *= 10;
  res += getColor(L4)*digit_place;
  digit_place *= 10;
  

  return res;
}

/**
 * Returns 0 for
 */
int getColor(int led[]) {
  if(isRed(led)) return RED;
  if(isBlue(led)) return BLUE;
  if(isGreen(led)) return GREEN;
  else return -1;
}



void makeRed(int led[]) {
  digitalWrite(led[0], HIGH);
  digitalWrite(led[1], LOW);
  digitalWrite(led[2], LOW);
}

void makeBlue(int led[]) {
  digitalWrite(led[0], LOW);
  digitalWrite(led[1], HIGH);
  digitalWrite(led[2], LOW);
}

void makeGreen(int led[]) {
  digitalWrite(led[0], LOW);
  digitalWrite(led[1], LOW);
  digitalWrite(led[2], HIGH);
}

void turnOff(int led[]) {
  for(int i = 0; i < 3; i++) {
    digitalWrite(led[i], LOW);
  }
}

bool isOff(int led[]) {
  return digitalRead(led[0]) == LOW && digitalRead(led[1]) == LOW && digitalRead(led[2]) == LOW;
}

bool isRed(int led[]) {
  return digitalRead(led[0]) == HIGH && digitalRead(led[1]) == LOW && digitalRead(led[2]) == LOW;
}

bool isBlue(int led[]) {
  return digitalRead(led[0]) == LOW && digitalRead(led[1]) == HIGH && digitalRead(led[2]) == LOW;
}

bool isGreen(int led[]) {
  return digitalRead(led[0]) == LOW && digitalRead(led[1]) == LOW && digitalRead(led[2]) == HIGH;
}

bool isOn(int led[]) {
  return !isOff(led);
}


void setup() {
  // put your setup code here, to run once:
  for(int i = 2; i < 14; i++) {
    if(i != 6)
    pinMode(i, OUTPUT);
  }
  pinMode(A5, OUTPUT);
  pinMode(But1, INPUT);
  pinMode(But2, INPUT);
  pinMode(But3, INPUT);
  pinMode(But4, INPUT);
}

void updateColor(int btn, int led[]) {
  int reading = digitalRead(btn);
  int pinToCheck = btn;
  if(btn == A0) pinToCheck = 3;
  if(btn == A1) pinToCheck = 4;
  // if the input just went from LOW and HIGH and we've waited long enough
  // to ignore any noise on the circuit, toggle the output pin and remember
  // the time
  if (reading == HIGH && saved[pinToCheck] == LOW && millis() - time > debounce) {
    nextColor(led);
    time = millis();    
  }

  saved[pinToCheck] = reading;
}

void onSetCode(int btn) {
  int reading = digitalRead(btn);

    if(reading == HIGH && saved[4] == LOW && millis() - time > debounce) {
      valToGuess = serialize();
      turnOff(L1);
      turnOff(L2);
      turnOff(L3);
      turnOff(L4);
      time = millis();
    }

    saved[5] = reading;
}

void checkGuess() {
  if(serialize() == valToGuess) {
    playWinSound();
  }
}

void reset() {
  valToGuess = -43924;
  turnOff(L1);
  turnOff(L2);
  turnOff(L3);
  turnOff(L4);
}

void playWinSound() {
    tone(tonePin,660,100);
    delay(150);
    tone(tonePin,660,100);
    delay(300);
    tone(tonePin,660,100);
    delay(300);
    tone(tonePin,510,100);
    delay(100);
    tone(tonePin,660,100);
    delay(300);
    tone(tonePin,770,100);
    delay(550);
    tone(tonePin,380,100);
    delay(575);
    reset();
}

void loop() {
  updateColor(But1, L1);
  updateColor(But2, L2);
  updateColor(But3, L3);
  updateColor(But4, L4);
  delay(50);

  onSetCode(SetBut);
  delay(50);
  checkGuess();
  delay(50);
}
