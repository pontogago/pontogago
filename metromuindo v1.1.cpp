#include <LiquidCrystal.h> // biblioteca do display lcd 16x2
// declaração pinos lcd

#define PIN_LCD_RS 9
#define PIN_LCD_EN 8
#define PIN_LCD_D4 7
#define PIN_LCD_D5 6
#define PIN_LCD_D6 5
#define PIN_LCD_D7 4

// GLOBAL DA BIBLIOTECA LIQUID-CRYSTAL

LiquidCrystal lcd(
PIN_LCD_RS,
PIN_LCD_EN,
PIN_LCD_D4,
PIN_LCD_D5,
PIN_LCD_D6,
PIN_LCD_D7
  );

  // animação inicio

byte metro1[8] = {
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
  B01000,
  B01110,
  B11111
  };

byte metro2[8] = {
  B00100,
  B00100,
  B00100, 
  B00100,
  B00100,
  B00100,
  B01110,
  B11111 
  };

byte metro3[8] = {
  B00001, 
  B00001,
  B00001, 
  B00001,
  B00001,
  B00010,
  B01110,
  B11111
  };

byte metro4[8] = {
  B00100,
  B00100,
  B00100,
  B00100,
  B00100,
  B00100,
  B01110,
  B11111 
  };

  


// declaração potenciometros

int ValorSensor = 0;
int nota = 0;

int valorsensor2 = 0;
int nota2 = 0;

// declaração pinos leds e buzzer
const int Buzzer = 3;

const int led1 = 13;
const int led2 = 12;
const int led3 = 11;
const int led4 = 10;

// configurações dos pinos botão de aumentar e abaixar o bpm
#define pin_btn_up 17
#define pin_btn_down 18

// variaveis global dos botoes
unsigned int bpm = 100;  // valor inicial do bpm
int btn_up   = LOW;
int btn_down = LOW; 

// configurações do botão de para ou inicar o metronomo

#define playstop 2
int pulso = 0;
int estado = 0;
int estadoatual = 0;

int valordaconta = 0;

void setup () {  //CONFIGURAÇÃO GERAL - VULGO SETUP
lcd.begin (16, 2);
Serial.begin(19200);

pinMode(Buzzer, OUTPUT);
pinMode(pin_btn_up, INPUT);
pinMode(pin_btn_down, INPUT);
pinMode(playstop, INPUT);
pinMode(led1, OUTPUT); 
pinMode(led2, OUTPUT);
pinMode(led3, OUTPUT); 
pinMode(led4, OUTPUT);

bemvindo();
  
  }

 void loop(){

valordaconta = 15000 / bpm;
  
  btn_botao();
  playpause();
  valsen();
  delay(10);

  
 }

 void valsen() {
ValorSensor = analogRead(A0);
valorsensor2 = analogRead(A2);

nota = map(ValorSensor, 0, 1023, 800, 3000);
nota2 = map(valorsensor2, 0, 1023, 440, 2000);
  
 }

 void playpause(){


pulso = digitalRead(playstop); // ler o pino 2 playstop

if ((pulso == HIGH) && (estado) == LOW){
  estadoatual = 1 - estadoatual;
  delay (1);
    }

    if (estadoatual == 1){
      anima();    
           }
  else { inicio();
  
    }
 }

void inicio(){
lcd.createChar(1, metro1);
lcd.createChar(2, metro2);
lcd.createChar(3, metro3);
lcd.createChar(4, metro4);
lcd.clear();
  
  lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO");
lcd.setCursor (0,1);
lcd.print ("PARA INICIAR ");
lcd.setCursor (15,1);
lcd.write (1);
digitalWrite(13, LOW);
digitalWrite(12, LOW);
digitalWrite(11, LOW);
digitalWrite(10, LOW);
  delay(200);
  
  lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO");
lcd.setCursor (0,1);
lcd.print ("PARA INICIAR ");
lcd.setCursor (15,1);
lcd.write (2);
  delay(200);

lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO");
lcd.setCursor (0,1);
lcd.print ("PARA INICIAR ");
lcd.setCursor (15,1);
lcd.write (3);
  delay(200);
  
  lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO");
lcd.setCursor (0,1);
lcd.print ("PARA INICIAR ");
lcd.setCursor (15,1);
lcd.write (4);
  delay(200);

  if (digitalRead(17) == HIGH && digitalRead(18) == HIGH) { // easter egg :)

    lcd.clear();
    lcd.setCursor (3,0);
    lcd.print ("EASTER EGG");
    lcd.setCursor (4,1);
    lcd.print ("ATIVADO");
     
    tone(Buzzer,262,200); delay(200); // DO
    tone(Buzzer,294,300); delay(200); // RE
    tone(Buzzer,330,300); delay(200); // MI
    tone(Buzzer,349,300); delay(300);
    tone(Buzzer,349,300); delay(300);
    tone(Buzzer,349,300); delay(300);
    tone(Buzzer,262,100); delay(200);
    tone(Buzzer,294,300); delay(200);   
    tone(Buzzer,262,100); delay(200);
    tone(Buzzer,294,300); delay(300);
    tone(Buzzer,294,300); delay(300);
    tone(Buzzer,294,300); delay(300);
    tone(Buzzer,262,200); delay(200);
    tone(Buzzer,392,200); delay(200);
    tone(Buzzer,349,200); delay(200);
    tone(Buzzer,330,300); delay(300);
    tone(Buzzer,330,300); delay(300);
    tone(Buzzer,330,300); delay(300);
    tone(Buzzer,262,200); delay(200);
    tone(Buzzer,294,300); delay(200);
    tone(Buzzer,330,300); delay(200);
    tone(Buzzer,349,300); delay(300);
    tone(Buzzer,349,300); delay(300);
    tone(Buzzer,349,300); delay(300);
    lcd.clear();

  }
}

 void anima(){

lcd.clear();
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (3,1);
lcd.print ("|O---DESLIGAR");
lcd.setCursor (0,1);
lcd.print (bpm);
tone(Buzzer, nota2, 20); 
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
btn_botao();
delay (valordaconta);

lcd.setCursor (3,1);
lcd.print ("|-O--DESLIGAR");
lcd.setCursor (0,1);
lcd.print (bpm);

tone(Buzzer, nota, 20); 
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
btn_botao();
delay (valordaconta);

lcd.setCursor (3,1);
lcd.print ("|--O-DESLIGAR");
lcd.setCursor (0,1);
lcd.print (bpm);
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
btn_botao();
delay (valordaconta);

lcd.setCursor (3,1);
lcd.print ("|---ODESLIGAR");
lcd.setCursor (0,1);
lcd.print (bpm);
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
btn_botao();
delay (valordaconta);
    if (bpm >= 400)
  {
    bpm = 100;
    delay(100);
  }

 }

  void btn_botao() {

    Serial.println(bpm);
int novoEstadoBotao;

novoEstadoBotao = digitalRead (pin_btn_up);
if (novoEstadoBotao == btn_up && novoEstadoBotao == HIGH){
  
  bpm ++;  
  }

  btn_up = novoEstadoBotao;

  //____________________________________________________

  novoEstadoBotao = digitalRead (pin_btn_down);
if (novoEstadoBotao == btn_down && novoEstadoBotao == HIGH){
  
  bpm--;  
  }

  btn_down = novoEstadoBotao;
   
    }

    void bemvindo(){

      lcd.clear();
      lcd.setCursor(2,0);
      lcd.print ("METROMUINDO");
      lcd.setCursor (3,1);
      lcd.print ("Ver. 1.13");
      delay(1500);
      lcd.clear();
      lcd.setCursor(2,0);
      lcd.print ("Create By");
      lcd.setCursor (0,1);
      lcd.print ("Harrison Aprigio");
      delay(1500);
      
    }
// simulador e esquem https://www.tinkercad.com/things/akCIh6BlQlH-metromuindo-v113
