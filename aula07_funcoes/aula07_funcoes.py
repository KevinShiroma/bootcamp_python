import csv
import pandas as pd 

# # Função simples
# def soma(num1, num2):
#     return num1 + num2

# print(soma(2,3))

# # É possivel chumbar os parâmetros
# def soma_valor_chumbado(num1, num2, texto="soma"):
#     print(f"sua {texto} deu {num1 + num2}")

# soma_valor_chumbado(10, 2)

##################################################################################
"""
Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas tot
"""
# Lendo um CSV
def ler_csv(caminho_csv):
    caminho_arquivo: str = caminho_csv
    arquivo_csv = []

    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)

        for linha in leitor_csv:
            arquivo_csv.append(linha)

    vendas_df = pd.DataFrame(arquivo_csv)
    return print(vendas_df)

ler_csv("tabela_aula07.csv")

def processar_dados():
    pass