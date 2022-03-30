class Encender_LED{
  private:
  int led;
  int valor = 0;
  int estado = 0;

  public:

  void setU(int led){
    pinMode(led, OUTPUT);
  }

  void encender(int led){
    estado = analogRead(A0);
    if(estado < (1023/2)){
      digitalWrite(led, LOW);
      valor = map(estado,0,1023,0,5);
      float voltaje = estado * (5.0/1023.0);
      Serial.println(voltaje);
    }
    else{
      if((estado >= (1023/2)) && estado < 1023){
        valor = map(estado,0,1023,0,5);
        float voltaje = estado * (5.0/1023.0);
        digitalWrite(led, valor);
        Serial.println(voltaje);
      }
      else{
        valor = map(estado,0,1023,0,5);
        float voltaje = estado * (5.0/1023.0);
        digitalWrite(led, valor);
        Serial.println(voltaje);
        delay(10);
        digitalWrite(led, LOW);
      }
    }
    delay(100);
  }
};
