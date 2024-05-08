/*
==============================================================================================================
projeto: arlaminio
criador por: Harrison Aprigio
data: 17/04/2018
===============================================================================================================

todos direitos resevados

copiar somente com esse comentario




===== Harrison Esdras Aprigio da Silva  ==============================================================
*/

#define sirene 2
#define status 12
#define btn 13


void setup()
{
  Serial.begin(9600);

  pinMode(btn, INPUT); // pino 13 ---pino do botão, chave tatil normalmente aberto, quando ativio fica normalmente fechado
  pinMode(status, OUTPUT); // pino 12 --- saida do led verde, led de indicação de estatus
  pinMode(sirene, OUTPUT); //pino 2--- saida do transistor NPN ( quaquer um transistor de potencia)
}

void loop()
{

  int valordoldr = analogRead(A0);
 float voltage = valordoldr * (5.0 / 1023.0);   Serial.println(voltage); Serial.print ("valor ldr  ");
  

  if (voltage > 0 && voltage < 0.49) // teste do sensor de luz, detectando a noite ------------- 
  
  {

    if (digitalRead(btn) == HIGH) {

      digitalWrite(status, LOW); // desativa o led verde


      digitalWrite(sirene, HIGH);
      delay(5200); // tempo da sirene para cortar as outras palavras fazendo reniciar --------- alterar para diferentes sirenes
      digitalWrite(sirene, LOW);
      delay(100); // reniciar a sirene desarmando por milesimos de segundo

    }


    if (digitalRead(btn) == LOW) {
      digitalWrite(status, HIGH);
      delay(500);
      digitalWrite(status, LOW);
      delay(200);
    }

  }
  if (voltage > 0.50 && voltage < 5) // teste do sensor de luz, detectando o dia, quando de dia não deixa o alarme disparar ------- descomentar

 {
    digitalWrite(sirene, LOW);
    delay(1);
    digitalWrite(status, HIGH);
    delay(200);
    digitalWrite(status, LOW);
    delay(100);

  }

}

// esquema e simulador https://www.tinkercad.com/things/aSiI4oyX6PX-alarminio-alarme-arduino
