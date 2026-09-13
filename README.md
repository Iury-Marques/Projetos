# 🛠️ Meus Projetos em Python

Coleção de scripts desenvolvidos para consolidar conceitos de automação de sistemas, consumo de APIs REST, manipulação de dados e lógica de programação.

---

### 🌡️ Simulador de Monitoramento de Temperatura
* **Descrição:** Simula a leitura contínua de um sensor térmico, realizando a classificação automática de status (*Normal*, *Alta*, *Baixa*) e a persistência dos históricos.
* **Tecnologias:** `csv`, `random`, `time`, `datetime`.
* **Conceitos aplicados:** Leitura/escrita de arquivos estruturados em CSV, tratamento de exceções (`KeyboardInterrupt`) e lógica de temporização.

### 📂 Organizador Automático de Arquivos
* **Descrição:** Script de automação para o sistema operacional que varre diretórios de entrada (como *Downloads*) e move arquivos automaticamente para pastas organizadas por extensão.
* **Tecnologias:** `os`, `shutil`.
* **Conceitos aplicados:** Manipulação de caminhos no SO (`os.path`), criação dinâmica de diretórios, mapeamento com dicionários e movimentação de arquivos.

### 💱 Consulta de Cotações em Tempo Real (API)
* **Descrição:** Cliente HTTP que consome a AwesomeAPI para obter a cotação atualizada do Dólar (USD) e Euro (EUR) em relação ao Real (BRL).
* **Tecnologias:** `requests`, REST API, JSON.
* **Conceitos aplicados:** Requisições HTTP GET, parsing de estruturas JSON encadeadas, tratamento de falhas de rede e formatação de dados numéricos.

### 📊 Calculadora de Média Acadêmica
* **Descrição:** Ferramenta para processamento e validação de notas, calculando a média final e determinando a situação de aprovação.
* **Tecnologias:** Python nativo.
* **Conceitos aplicados:** Estruturas condicionais, entrada/saída de dados no terminal e fundamentos da lógica de programação.