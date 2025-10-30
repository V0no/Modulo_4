# Projeto: Semáforo para Controle de Trânsito (Butantã)

Resumo: montagem e programação de um semáforo com LEDs para controle de fluxo de veículos e segurança de pedestres. Ciclo implementado: vermelho → verde → amarelo com tempos especificados.

---

## Parte 1: Montagem Física do Semáforo

Materiais:
- 1x Arduino (qualquer modelo)
- 1x LED vermelho
- 1x LED amarelo
- 1x LED verde
- 3x resistores 220 Ω
- Protoboard e jumpers
- Fonte USB para o Arduino

Esquema de ligação (resumo):
- LED vermelho: anodo -> pino digital 8 (via resistor 220 Ω), catodo -> GND
- LED amarelo: anodo -> pino digital 9 (via resistor 220 Ω), catodo -> GND
- LED verde: anodo -> pino digital 10 (via resistor 220 Ω), catodo -> GND

Dicas:
- Sempre coloque o resistor no anodo do LED para limitar corrente.
- Organize fios por cor para facilitar inspeção (Vermelho, Amarelo, Verde, GND).
- Verifique polaridades antes de energizar.

---

## Parte 2: Programação e Lógica do Semáforo

Requisitos de temporização:
- $6\ \text{s}$ no vermelho
- $4\ \text{s}$ no verde
- $2\ \text{s}$ no amarelo

Lógica implementada: ciclo contínuo com tempos fixos usando millis() para evitar bloqueios por delay().

Código usado (arquivo no repositório: [Semana_03/Semaforo/Semaforo.ino](Semana_03/Semaforo/Semaforo.ino)):

```ino
// filepath: 
// Semáforo com millis()

const int VERMELHO = 8;
const int AMARELO = 9;
const int VERDE = 10;

// tempos em milissegundos
const unsigned long TEMPO_VERDE = 4000;
const unsigned long TEMPO_AMARELO = 2000;
const unsigned long TEMPO_VERMELHO = 6000;

unsigned long tempoAnterior = 0;  // registra quando mudou o sinal
int estado = 0; // 0 = verde, 1 = amarelo, 2 = vermelho

void setup() {
  pinMode(VERMELHO, OUTPUT);
  pinMode(AMARELO, OUTPUT);
  pinMode(VERDE, OUTPUT);
}

void loop() {
  unsigned long agora = millis();

  switch (estado) {
    case 0: // verde
      digitalWrite(VERDE, HIGH);
      digitalWrite(AMARELO, LOW);
      digitalWrite(VERMELHO, LOW);
      if (agora - tempoAnterior >= TEMPO_VERDE) {
        estado = 1; // muda para amarelo
        tempoAnterior = agora;
      }
      break;

    case 1: // amarelo
      digitalWrite(VERDE, LOW);
      digitalWrite(AMARELO, HIGH);
      digitalWrite(VERMELHO, LOW);
      if (agora - tempoAnterior >= TEMPO_AMARELO) {
        estado = 2; // muda para vermelho
        tempoAnterior = agora;
      }
      break;

    case 2: // vermelho
      digitalWrite(VERDE, LOW);
      digitalWrite(AMARELO, LOW);
      digitalWrite(VERMELHO, HIGH);
      if (agora - tempoAnterior >= TEMPO_VERMELHO) {
        estado = 0; // volta para verde
        tempoAnterior = agora;
      }
      break;
  }
}