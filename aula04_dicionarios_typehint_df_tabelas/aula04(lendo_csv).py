# Lendo um CSV
import csv
import pandas as pd # type: ignore

caminho_arquivo: str = "tabela04.csv"

arquivo_csv = []

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

df = pd.DataFrame(arquivo_csv)
print(df)