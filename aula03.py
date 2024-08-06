# DEBUG, IF, FOR, While, Listas e Dicionários em Python

# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

quantidade = 10
preco = 2

if quantidade > 0 and preco > 0:
    print("valores corretos")
else:
    print("valores incorretos")

#     Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura: float = 17
if temperatura < 18:
    print("Baixa")
elif temperatura >= 18 and temperatura <=26:
    print("Normal")
else:
    print("Alta")


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == "ERROR":
    print(log['message'])

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 20
email = "usuario2email.com"

if idade > 18 and idade < 65:
    if "@" in email:
        print("cadastro efetuado com sucesso")
    else:
        print("Erro no email")
else:
    print("Idade inválida")


# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

transacao = {'valor': 9000, 'hora': 17}

if transacao['valor'] > 10000 and transacao['hora'] < 9 or transacao['hora']> 18:
    print("Atividade suspeita")
else:
    print("Transação normal")

#     6. Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes uma determinada palavra se repete.

frase = "hoje comi uma maçã, mas a maçã estava farinhenta, então peguei outra maçã"
palavra = "maçã"

frase_separada = frase.split()
count = 0
print(frase_separada)

for item in frase_separada:
    if item.strip(",.") == palavra:
        count = count + 1

print(f"A {palavra} apareceu {count} vezes")


# 7. Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

# 8. Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

# 9. Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# 11. Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.


while palavra != "sair":
    print(f"a palavra é {palavra}")
    palavra = input("palavra fornecida: ")

# 12. Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

tentativa = int(input("Escolha um numero: "))
numero_sorteado = 3

while tentativa != numero_sorteado:
    tentativa = int(input("Escolha um numero: "))

