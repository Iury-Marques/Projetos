import csv
import random
import time
from datetime import datetime

SensorTemperatura = "SensorTemperatura.csv"

try:
    with open(SensorTemperatura, mode='x', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['data_hora', 'Temperatura', 'Status'])
        print(f"Arquivo 'SensorTemperatura' criado com sucesso!")
except FileExistsError:
    print(f"Erro ao criar o arquivo '{SensorTemperatura}', arquivo existente. Novos dados serão adicionados ao arquivo.\n")
    print("-- Iniciando a simulação de leitura de temperatura do sensor. --\n")

try:
    while True:
        temperatura = round(random.uniform(10.0, 30.0), 2)

        if temperatura > 27.0:
            status = "Temperatura Alta"
        elif temperatura < 22.0:
            status = "Temperatura Baixa"
        else:
            status = "Normal"

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(SensorTemperatura, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([data_hora, temperatura, status])

        print(f"Data/Hora: {data_hora}, Temperatura: {temperatura}°C, Status: {status}")
        time.sleep(5)

except KeyboardInterrupt:
    print("\nSimulação encerrada pelo usuário.")