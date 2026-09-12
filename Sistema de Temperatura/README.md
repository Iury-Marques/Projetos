# 🌡️ Sistema de Monitoramento e Simulação de Sensor de Temperatura

Script em Python desenvolvido para simular a leitura contínua de um sensor de temperatura, realizando a classificação automática de status e o registro histórico dos dados em um arquivo `.csv`.

---

### 🚀 Funcionalidades

* **Leitura Dinâmica:** Simulação de medições de temperatura com variação contínua de dados.
* **Classificação em Tempo Real:** Análise lógica para categorização de alertas (*Normal*, *Temperatura Alta* e *Temperatura Baixa*).
* **Persistência de Dados:** Criação e alimentação automática do arquivo `SensorTemperatura.csv` sem sobrescrever registros antigos.
* **Tratamento de Exceções:** Gerenciamento de arquivos existentes (`FileExistsError`) e encerramento limpo da execução via teclado (`KeyboardInterrupt`).

---

### 🛠️ Tecnologias e Módulos Utilizados

* **Python 3**
* `csv` — Manipulação e exportação de dados estruturados em planilha.
* `random` — Geração das leituras numéricas simuladas.
* `time` — Controle do intervalo de tempo entre as medições.
* `datetime` — Registro de data e hora exatas de cada leitura.

---

### 📊 Estrutura dos Dados Exportados

Os dados são salvos no arquivo `SensorTemperatura.csv` seguindo o formato abaixo:

| Data_Hora | Temperatura | Status |
| :--- | :--- | :--- |
| 2026-09-12 15:30:00 | 23.45 | Normal |
| 2026-09-12 15:30:05 | 28.10 | Temperatura Alta |
| 2026-09-12 15:30:10 | 21.30 | Temperatura Baixa |

---

### 💻 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou clone os arquivos deste repositório na sua máquina.
3. Abra o terminal na pasta do projeto e execute o comando:

```bash
python simulador.py