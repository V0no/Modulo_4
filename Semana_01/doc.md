# Documentação Semana 01 - Introdução ao Arduino

## 📋 Visão Geral
Este projeto consiste em duas implementações básicas de controle de LED usando Arduino, demonstrando os fundamentos de programação com microcontroladores.

## 🎯 Objetivos
- Compreender o funcionamento básico do Arduino
- Implementar controle digital de LED
- Aprender sobre as funções setup() e loop()
- Entender o conceito de entrada/saída digital

## 📁 Estrutura do Projeto
```
Semana_01/
│
├── Blink/
│   ├── Blink.ino      # Programa de pisca LED builtin
│   └── Blink.txt      # Descrição do programa
│
├── Pisca/
│   └── Pisca.ino      # Programa de pisca LED externo
│
├── demosntracao.mp4   # Vídeo demonstrativo
├── print_code.png     # Captura de tela do código
└── Screenshot_2.png   # Captura de tela adicional
```

## 💻 Códigos Implementados

### 1. Blink (LED Integrado)
```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```
- **Objetivo**: Piscar o LED integrado da placa Arduino
- **Intervalo**: 1 segundo aceso, 1 segundo apagado
- **Pino utilizado**: LED_BUILTIN (LED integrado)

### 2. Pisca (LED Externo)
```cpp
void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  digitalWrite(9, 1);
  delay(500);
  digitalWrite(9, 0);
  delay(500);
}
```
- **Objetivo**: Controlar LED externo
- **Intervalo**: 0.5 segundo aceso, 0.5 segundo apagado
- **Pino utilizado**: Digital 9

## 🔧 Hardware Necessário
- 1x Arduino (qualquer modelo)
- 1x LED
- 1x Resistor 220Ω
- Cabos jumper

## 📝 Instruções de Montagem
1. **Para o Blink:**
   - Nenhuma montagem necessária (usa LED integrado)

2. **Para o Pisca:**
   - Conecte o LED ao pino digital 9
   - Adicione o resistor em série
   - Conecte o outro terminal ao GND

## ▶️ Como Executar
1. Abra o Arduino IDE
2. Carregue o arquivo desejado (Blink.ino ou Pisca.ino)
3. Selecione a placa Arduino correta
4. Selecione a porta COM apropriada
5. Clique em "Upload"

## 📚 Conceitos Aprendidos
- Configuração de pinos digitais
- Funções básicas do Arduino (setup/loop)
- Controle digital (HIGH/LOW)
- Temporização com delay()

## 🎥 Materiais Complementares
- `demosntracao.mp4`: Vídeo mostrando o funcionamento
- `print_code.png`: Captura do código fonte
- `Screenshot_2.png`: Captura da interface

## ⚠️ Observações Importantes
- Verifique a polaridade do LED ao conectar
- Não exceda a corrente máxima do pino (20mA)
- O delay() pausa toda a execução do programa

## 🎯 Experiência com o Projeto

### Primeiros Passos com Arduino
Esta foi minha primeira experiência prática com Arduino, onde pude aprender conceitos fundamentais de programação em microcontroladores. O projeto, embora simples, proporcionou aprendizados valiosos sobre:

- Configuração inicial do ambiente Arduino IDE
- Compreensão do ciclo setup() e loop()
- Manipulação de pinos digitais
- Conceitos básicos de eletrônica

### Desafios Encontrados
- Familiarização com a sintaxe específica do Arduino
- Entendimento do funcionamento dos pinos digitais
- Configuração correta da placa e porta no IDE

### Aprendizados
1. A importância do resistor para proteger o LED
2. Como o delay() afeta a execução do programa
3. Diferenças entre usar o LED integrado e um LED externo
4. Boas práticas de programação em Arduino

### Próximos Passos
Para evoluir este projeto, pretendo:
- Adicionar mais LEDs para criar sequências
- Implementar botões para controle
- Explorar o uso de sensores
- Criar projetos mais complexos com múltiplos componentes