// Semáforo com millis() e ponteiros

const int VERMELHO = 8;
const int AMARELO = 9;
const int VERDE = 10;

// tempos em milissegundos
const unsigned long TEMPO_VERDE = 6000;
const unsigned long TEMPO_AMARELO = 2000;
const unsigned long TEMPO_VERMELHO = 4000;

unsigned long tempoAnterior = 0;  // registra quando mudou o sinal
int estado = 0; // 0 = verde, 1 = amarelo, 2 = vermelho

// Ponteiros para os pinos
const int* pinoVermelho = &VERMELHO;
const int* pinoAmarelo  = &AMARELO;
const int* pinoVerde    = &VERDE;

void setup() {
  // Usa o valor dos ponteiros com o operador '*'
  pinMode(*pinoVermelho, OUTPUT);
  pinMode(*pinoAmarelo, OUTPUT);
  pinMode(*pinoVerde, OUTPUT);
}

void loop() {
  unsigned long agora = millis();

  switch (estado) {
    case 0: // verde
      digitalWrite(*pinoVerde, HIGH);
      digitalWrite(*pinoAmarelo, LOW);
      digitalWrite(*pinoVermelho, LOW);
      
      if (agora - tempoAnterior >= TEMPO_VERDE) {
        estado = 1; // muda para amarelo
        tempoAnterior = agora;
      }
      break;

    case 1: // amarelo
      digitalWrite(*pinoVerde, LOW);
      digitalWrite(*pinoAmarelo, HIGH);
      digitalWrite(*pinoVermelho, LOW);
      
      if (agora - tempoAnterior >= TEMPO_AMARELO) {
        estado = 2; // muda para vermelho
        tempoAnterior = agora;
      }
      break;

    case 2: // vermelho
      digitalWrite(*pinoVerde, LOW);
      digitalWrite(*pinoAmarelo, LOW);
      digitalWrite(*pinoVermelho, HIGH);
      
      if (agora - tempoAnterior >= TEMPO_VERMELHO) {
        estado = 0; // volta para verde
        tempoAnterior = agora;
      }
      break;
  }
}
