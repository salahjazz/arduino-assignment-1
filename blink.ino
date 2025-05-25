// Blink with errors - Students must fix it

void setup() {
  pinMode(LED_BUILTIN, INPUT);  // خطأ: المفروض OUTPUT بدل INPUT
}

void loop() {
  digitalWrite(LED_BUILTIN, LOW);   // خطأ: المفروض HIGH لتشغيل LED
  delay(500);                       // نصف ثانية تأخير
  digitalWrite(LED_BUILTIN, HIGH);  // خطأ: المفروض LOW لإطفاء LED
  delay(500);                       // نصف ثانية تأخير
}
