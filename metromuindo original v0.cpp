// DECLARAÇÃO DAS VARIAVEIS 
#include <LiquidCrystal.h>

const int  pot = A1;
int valpot = 0;

int valorsensor2 = 0;
int nota2 = 0;

int ValorSensor = 0;
int nota = 0;
const int Buzzer = 3;

const int led1 = 13;
const int led2 = 12;
const int led3 = 11;
const int led4 = 10;

// display

#define PIN_LCD_RS       9
#define PIN_LCD_EN       8
#define PIN_LCD_D4       7 
#define PIN_LCD_D5       6
#define PIN_LCD_D6       5 
#define PIN_LCD_D7       4

LiquidCrystal lcd(
    PIN_LCD_RS,
    PIN_LCD_EN,
    PIN_LCD_D4,
    PIN_LCD_D5,
    PIN_LCD_D6,
    PIN_LCD_D7
);

int playstop = 2; // saida do pino
int pulso = 0;     // valor do pulso
int estado = 0;    // valor guardado
int estadoatual =0; // guarda high ou low

void setup(){
 
  
  pinMode(led1, OUTPUT); pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT); pinMode(led4, OUTPUT);
   Serial.begin(9600);
   lcd.begin(16, 2);

   pinMode(playstop, INPUT);
}

void loop(){

pulso = digitalRead(playstop); // ler o pino 2 playstop

if ((pulso == HIGH) && (estado) == LOW){
  estadoatual = 1 - estadoatual;
  delay (20);
}

if (estadoatual == 1){
  
ValorSensor = analogRead(A0);
valorsensor2 = analogRead(A2);

nota = map(ValorSensor, 0, 1023, 800, 3000);
nota2 = map(valorsensor2, 0, 1023, 440, 2000);
valpot = analogRead(pot);

float voltage = valpot * (5.0 / 1023);

Serial.println(voltage);

if (voltage<0.5) {
  
 lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print (" 60|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 60bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(250);   
    
lcd.setCursor (0,1);
lcd.print (" 60|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(250); 
 

lcd.setCursor (0,1);
lcd.print (" 60|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(250); 

 
lcd.setCursor (0,1);
lcd.print (" 60|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(250); 
  
}

if (voltage>0.5 && voltage <1) {

lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print (" 70|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 70 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(214.2);

lcd.setCursor (0,1);
lcd.print (" 70|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(214.2);

lcd.setCursor (0,1);
lcd.print (" 70|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(214.2);

lcd.setCursor (0,1);
lcd.print (" 70|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(214.2);
  
}
if (voltage>1 && voltage <1.5) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print (" 80|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 80 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(187.5);

lcd.setCursor (0,1);
lcd.print (" 80|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(187.5);

lcd.setCursor (0,1);
lcd.print (" 80|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(187.5);

lcd.setCursor (0,1);
lcd.print (" 80|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(187.5);
  
}
if (voltage>1.5 && voltage <2) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print (" 90|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 90 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(166.6);

lcd.setCursor (0,1);
lcd.print (" 90|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(166.6);

lcd.setCursor (0,1);
lcd.print (" 90|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(166.6);

lcd.setCursor (0,1);
lcd.print (" 90|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(166.6);
  
}
if (voltage>2 && voltage <2.5) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print ("100|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 100 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(150.0);

lcd.setCursor (0,1);
lcd.print ("100|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(150.0);

lcd.setCursor (0,1);
lcd.print ("100|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(150.0);

lcd.setCursor (0,1);
lcd.print ("100|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(150.0);
  
}
if (voltage>2.5 && voltage <3) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print ("110|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 110 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(136.3);

lcd.setCursor (0,1);
lcd.print ("110|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(136.3);

lcd.setCursor (0,1);
lcd.print ("110|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(136.3);

lcd.setCursor (0,1);
lcd.print ("110|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(136.3);
  
}
if (voltage>3 && voltage <3.5) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print ("120|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 120 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(125.0);

lcd.setCursor (0,1);
lcd.print ("120|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(125.0);

lcd.setCursor (0,1);
lcd.print ("120|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(125.0);

lcd.setCursor (0,1);
lcd.print ("120|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(125.0);
  
}
if (voltage>3.5 && voltage <4) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print ("130|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 130 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(115.3);

lcd.setCursor (0,1);
lcd.print ("130|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(115.3);

lcd.setCursor (0,1);
lcd.print ("130|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(115.3);

lcd.setCursor (0,1);
lcd.print ("130|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(115.3);
  
}

if (voltage>4 && voltage <4.5) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print ("140|O---DESLIGAR");

tone(Buzzer, nota2, 20);   // 140 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(107.1);

lcd.setCursor (0,1);
lcd.print ("140|-O--DESLIGAR");
tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(107.1);

lcd.setCursor (0,1);
lcd.print ("140|--O-DESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(107.1);

lcd.setCursor (0,1);
lcd.print ("140|---ODESLIGAR");
tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(107.1);
  
}
if (voltage>4.5 && voltage <5.5) {
lcd.setCursor (0,0);
lcd.print ("BPM| APERTE PARA");
lcd.setCursor (0,1);
lcd.print ("150|O---DESLIGAR");


tone(Buzzer, nota2, 20);   // 150 bmp
digitalWrite(10, LOW);
digitalWrite(13, HIGH);
delay(100);

lcd.setCursor (0,1);
lcd.print ("150|-O--DESLIGAR");

tone(Buzzer, nota, 20); //
digitalWrite(13, LOW);
digitalWrite(12, HIGH);
delay(100);

lcd.setCursor (0,1);
lcd.print ("150|--O-DESLIGAR");

tone(Buzzer, nota, 20);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
delay(100);

lcd.setCursor (0,1);
lcd.print ("150|---ODESLIGAR");

tone(Buzzer, nota, 20);
digitalWrite(11, LOW);
digitalWrite(10, HIGH);
delay(100);
  
}

} else {
lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO P/");
lcd.setCursor (0,1);
lcd.print ("INICIAR       )(");
digitalWrite(13, LOW);
digitalWrite(12, LOW);
digitalWrite(11, LOW);
digitalWrite(10, LOW);
  delay(200);
  lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO P/");
lcd.setCursor (0,1);
lcd.print ("INICIAR       ||");
digitalWrite(13, LOW);
digitalWrite(12, LOW);
digitalWrite(11, LOW);
digitalWrite(10, LOW);
  delay(200);

lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO P/");
lcd.setCursor (0,1);
lcd.print ("INICIAR       ()");
digitalWrite(13, LOW);
digitalWrite(12, LOW);
digitalWrite(11, LOW);
digitalWrite(10, LOW);
  delay(200);
  lcd.setCursor (0,0);
lcd.print ("APERTE O BOTAO P/");
lcd.setCursor (0,1);
lcd.print ("INICIAR       ||");
digitalWrite(13, LOW);
digitalWrite(12, LOW);
digitalWrite(11, LOW);
digitalWrite(10, LOW);
  delay(200);

}

}

// esquema e simulador https://www.tinkercad.com/things/6RpURTalmtf-metromuindo-original
