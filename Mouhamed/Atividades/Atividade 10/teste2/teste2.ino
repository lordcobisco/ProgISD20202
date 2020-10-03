//funcionando no serial
const int RelePin = 7; // pino ao qual o Módulo Relé está conectado
int incomingByte;      // variavel para ler dados recebidos pela serial

void setup() {
  Serial.begin(9600); // inicializa a comunicação serial em 9600bps
  pinMode(RelePin, OUTPUT); // seta o pino como saída 

  digitalWrite(RelePin, HIGH); //Estado inicial dos reles - desligados

  Serial.println("Bem vind@ a Neurobots! Sua sessão de FES está pronta para ser iniciada");
  Serial.println("Digite 'S' para iniciar a estimulação e 'N' para desligar a estimulação");
}


void loop() {
  if (Serial.available() > 0) {
    // verifica se tem algum dado na serial
    incomingByte = Serial.read();  //lê o primeiro dado do buffer da serial

    if (incomingByte == 'S') {     //se for A
      digitalWrite(RelePin, LOW); //aciona o pino
      Serial.println("FES LIGADO");
    } 

    if (incomingByte == 'N') {     //se for D
      digitalWrite(RelePin, HIGH);  //desativa o pino
      Serial.println("FES DESLIGADO");
    }
  }
}
