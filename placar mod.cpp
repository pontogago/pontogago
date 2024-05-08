#include <LiquidCrystal.h>

// Configurações de pinos

#define PIN_LCD_D7        8
#define PIN_LCD_D6        9
#define PIN_LCD_D5       10
#define PIN_LCD_D4       11
#define PIN_LCD_EN       12
#define PIN_LCD_RS       13

#define PIN_BTN_1         7
#define PIN_BTN_2         6
#define PIN_BTN_3         5
#define PIN_BTN_4         4

#define spk    3
/*
 * GLOBAIS
 */

// Inicializa o objeto LCD configurando os pinos de comunicação
LiquidCrystal lcd(
    PIN_LCD_RS,
    PIN_LCD_EN,
    PIN_LCD_D4,
    PIN_LCD_D5,
    PIN_LCD_D6,
    PIN_LCD_D7
);

// Configurações dos jogadores e placar
const char firstPlayerName[] = "time floresta ";
unsigned int firstPlayerScore = 0;
int firstButtonState = LOW;
int thirdButtonState = LOW;

const char secondPlayerName[] = "time     casa ";
unsigned int secondPlayerScore = 0;
int secondButtonState = LOW;
int quarterButtonState = LOW;

void setup() {
    setupInputs();
    setupLCD();
    printWelcome();
    
    tone(spk,261); delay(300); noTone(spk); // dó
      
    tone(spk,294); delay(300); noTone(spk); // ré
    
    tone(spk,329); delay(300); noTone(spk); // mi 
       
    delay(1000);
}

void loop() {
    checkButtons();
    printScore();

    delay(100);
}

void setupInputs()
{
    pinMode(PIN_BTN_1, INPUT);
    pinMode(PIN_BTN_2, INPUT);
    pinMode(PIN_BTN_3, INPUT);
    pinMode(PIN_BTN_4, INPUT);
}

void setupLCD()
{
    // Configura o tamanho do LCD: 16 colunas e 2 linhas
    lcd.begin(16, 2);
}

void printWelcome()
{
    lcd.clear();
    // Posiciona o cursor na primeira coluna da primeira linha
    lcd.setCursor(2, 0);
    lcd.print("PLACA ARDUINO");
    // Posiciona o cursor na terceira coluna da segunda linha
    lcd.setCursor(0, 1);
    lcd.print("Mod. Herrinho:-)");
}

void checkButtons()
{                          //INICIO PARENTESES DA VOID CHECKBUTTONS
    int newButtonState;

    newButtonState = digitalRead(PIN_BTN_1);
    if (newButtonState != firstButtonState && newButtonState == HIGH) {
        // Se o botão mudou de estado e o novo estado é pressionado, soma um ponto
        firstPlayerScore++;
        tone(spk,261);    
        delay(100);
        noTone(spk);
    }
    firstButtonState = newButtonState;

// ----------------------------------------------------------------- //

    newButtonState = digitalRead(PIN_BTN_2);
    if (newButtonState != secondButtonState && newButtonState == HIGH) {
         secondPlayerScore++;
     tone(spk,440);   // som da nota A (LA) 
     delay(100);
     noTone(spk);
    }
    secondButtonState = newButtonState;
// ----------------------------------------------------------------- //
    newButtonState = digitalRead(PIN_BTN_3);
    if (newButtonState != thirdButtonState && newButtonState == HIGH){
        firstPlayerScore--;
        tone(spk, 329);
        delay(100);
        noTone(spk);
        }
        thirdButtonState = newButtonState;
// -----------------------------------------------------------------//
   newButtonState = digitalRead(PIN_BTN_4);
   if (newButtonState != quarterButtonState && newButtonState == HIGH){
      secondPlayerScore--;
      tone(spk, 587);
      delay(100);
      noTone(spk);
      }
// -----------------------------------------------------------------//
}                     // FINAL PARENTESES DA VOID CHECKBUTTONS

void printScore()
{
    // Buffer para saída do dtostrf
    // Usado para formatar os pontos alinhados à direita
    char outScore[4];

    lcd.clear();

    lcd.setCursor(0, 0);
    lcd.print(firstPlayerName);
    lcd.setCursor(13, 0);
    lcd.print(dtostrf(firstPlayerScore, 3, 0, outScore));

    lcd.setCursor(0, 1);
    lcd.print(secondPlayerName);
    lcd.setCursor(13, 1);
    lcd.print(dtostrf(secondPlayerScore, 3, 0, outScore));
}

// esquema e simulador https://www.tinkercad.com/things/cJ6z681JdQQ-placar
