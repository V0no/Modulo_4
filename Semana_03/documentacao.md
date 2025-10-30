# Projeto: Semáforo 

Resumo: Montagem e programação de um semáforo com LEDs para controle de fluxo de veículos e segurança de pedestres. Ciclo implementado: vermelho → verde → amarelo com tempos especificados utilizando millis() para controle não bloqueante.

---

## Parte 1: Montagem Física do Semáforo

### Materiais
- 1x Arduino (qualquer modelo)
- 1x LED vermelho
- 1x LED amarelo
- 1x LED verde
- 3x resistores 220 Ω
- Protoboard e jumpers
- Cabo USB para alimentação e programação

### Esquema de ligação
- LED vermelho: anodo -> pino digital 8 (via resistor 220 Ω), catodo -> GND
- LED amarelo: anodo -> pino digital 9 (via resistor 220 Ω), catodo -> GND
- LED verde: anodo -> pino digital 10 (via resistor 220 Ω), catodo -> GND

### Boas práticas de montagem
- Utilizar resistores em série com os LEDs para limitar corrente.
- Padronizar as cores dos jumpers para facilitar inspeção e depuração.
- Confirmar polaridade dos LEDs e continuidade das ligações antes de energizar o circuito.

---

## Parte 2: Programação e Lógica do Semáforo

### Requisitos de temporização
- 6 segundos no vermelho
- 4 segundos no verde
- 2 segundos no amarelo

### Metodologia
O ciclo do semáforo foi implementado com base no controle de tempo utilizando a função `millis()`. Esse método evita bloqueios no fluxo do programa e permite expansões futuras, como detecção de pedestres ou sensores de tráfego, sem interromper a execução.

---

### Código Fonte
Arquivo no repositório: `Semana_03/Semaforo/Semaforo.ino`

```ino
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

```


## Parte 3: Avaliação de Pares

### Critérios de Avaliação

Os colegas avaliadores devem analisar:

- Clareza e organização da montagem física
- Uso correto de resistores e conexões elétricas
- Conformidade dos tempos implementados com os requisitos
- Clareza da explicação, imagens e/ou vídeo de demonstração
- Evidência de autoria no vídeo e documentação

---

### Tabela de Componentes

| Componente     | Quantidade | Especificação      |
|----------------|-----------:|--------------------|
| Arduino        | 1          | Uno / compatível   |
| LED vermelho   | 1          | 5mm                |
| LED amarelo    | 1          | 5mm                |
| LED verde      | 1          | 5mm                |
| Resistores     | 3          | 220 Ω              |
| Protoboard     | 1          | -                  |
| Jumpers        | -          | -                  |

---

### Tabela de Avaliação de Pares

| Nome do Avaliador | Comentários | Nota (0–10) |
|-------------------|------------|-------------|
| Felipe Viana | O projeto apresenta boa organização, explicação clara da montagem e uso correto dos componentes. A escolha por millis() ao invés de delay() demonstra domínio de lógica não bloqueante, permitindo expansões futuras. A inclusão de ponteiros agrega complexidade extra, embora não seja estritamente necessária para o contexto, o que mostra intenção de explorar recursos mais avançados da linguagem. Porém durante a montagem não foi utilizado os jumpers com as cores corretas. |9.5  |
| Enzo Matsui | A documentação está bem estruturada e facilita a compreensão. Os tempos de cada estágio foram claramente definidos e implementados. O uso da máquina de estados torna o código limpo e modular. Embora o projeto esteja bem completo, durante a montagem poderia ter utilizado melhor as boas práticas, como por exemplo o uso das cores corretas nos jumpers |9  |

---

### Conclusão

O projeto alcançou o objetivo de simular um semáforo funcional com controle de tempo preciso e lógica não bloqueante. A utilização da função `millis()` garante execução contínua do código, sem bloqueios, permitindo futuras melhorias como sensor de presença, botoeira para pedestres ou integração com sistemas de tráfego inteligentes.
