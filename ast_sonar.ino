#define POT_PIN 34
#define BUTTON1 25
#define BUTTON2 26

int powerLevel = 50;
int mode = 0;

bool lastButton1 = HIGH;
bool lastButton2 = HIGH;

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON1, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
}

void loop() {

  int potValue = analogRead(POT_PIN);

  int frequency = map(potValue, 0, 4095, 500, 5000);

  // BUTTON 1 — manual power
  bool button1 = digitalRead(BUTTON1);

  if (lastButton1 == HIGH && button1 == LOW) {
    powerLevel += 10;

    if (powerLevel > 100) {
      powerLevel = 10;
    }

    delay(200);
  }

  lastButton1 = button1;


  // BUTTON 2 — mode selection
  bool button2 = digitalRead(BUTTON2);

  if (lastButton2 == HIGH && button2 == LOW) {
    mode++;

    if (mode > 2) {
      mode = 0;
    }

    delay(200);
  }

  lastButton2 = button2;


  // LOW POWER MODE automatically limits power
  int actualPower = powerLevel;

  if (mode == 2) {
    actualPower = 30;
  }


  // DISPLAY
  Serial.println();
  Serial.println("================================");
  Serial.println("          AST - SONAR");
  Serial.println("================================");

  Serial.print("Frequency : ");
  Serial.print(frequency);
  Serial.println(" Hz");

  Serial.print("Power     : ");
  Serial.print(actualPower);
  Serial.println(" %");

  Serial.print("Mode      : ");

  if (mode == 0) {
    Serial.println("NORMAL");
  }
  else if (mode == 1) {
    Serial.println("ADAPTIVE");
  }
  else {
    Serial.println("LOW POWER");
  }

  Serial.println("TX Status : READY");
  Serial.println("================================");

  delay(300);
}