# Exercícios
# Inteiros (int)
# Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# print("Exercício 1")
x = int(input("numero1: "))
y = int(input("numero2: "))
soma = x + y
print(soma)

# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# print("Exercício 2")
x = int(input("numero: "))
calculo = x % 5
print(calculo)

# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# print("Exercício 3") 
x = int(input("numero1: "))
y = int(input("numero2: "))
multiplicacao = x * y
print(multiplicacao)

# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# print("Exercício 4") 
x = int(input("numero1: "))
y = int(input("numero2: "))
divisao = x // y
print(divisao)

# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# print("Exercício 5")
x = int(input("numero: "))
calculo_quadrado = x ** 2
print(calculo_quadrado)


# Números de Ponto Flutuante (float)
# Escreva um programa que receba dois números flutuantes e realize sua adição.
# print("Exercício 6")
x = float(input("numero1: "))
y = float(input("numero2: "))
soma = x + y
print(soma)


# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# print("Exercício 7")
x = float(input("numero1: "))
y = float(input("numero2: "))
media = (x + y) / 2
print(media)


# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# print("Exercício 8")
base = float(input("numero: "))
potencia = int(input("numero_potencia: "))
calculo_potencia = base ** potencia
print(calculo_potencia)


# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# print("Exercício 9")
valor_celsius = int(input("valor celsius: "))
calculo_conversao = (valor_celsius * 9 / 5 ) + 32
print(calculo_conversao)

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# print("Exercício 10")
raio = float(input("valor do raio: "))
area = (raio ** 2) * 3.14
print(area)


# Strings (str)
# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# print("Exercício 11")
palavra = input("palavra: ")
print(palavra.upper())

# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# print("Exercício 12")
nome = input("nome: ")
print(nome.lower())

# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# print("Exercício 13")
frase = input("insita a frase: ")
print(frase.strip())

# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# print("Exercício 14")
data = input("Insira a data: ")
dia, mes, ano = data.split("/")
print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")

# Escreva um programa que concatene duas strings fornecidas pelo usuário.
# print("Exercício 15")
palavra1 = input("palavra: ")
palavra2 = input("palavra2: ")
print(f"a primera palabra é {palavra1} e a segunda é {palavra2}")


# Booleanos (bool)
# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# print("Exercício 16")
x = True
y = False
print(x and y)

# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# print("Exercício 17")
x = True
y = False
print(x or y)

# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# print("Exercício 18")
x = True
print(not x)

# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# print("Exercício 19")
x = int(input("numero1: "))
y = int(input("numero2: "))
if x == y:
    print("Os números são iguais")
else:
    print("Os números NÃO são iguais")

# # Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# print("Exercício 20")
x = int(input("numero1: "))
y = int(input("numero2: "))
if x != y:
    print("Os números são diferentes")
else:
    print("Os números são IGUAIS")

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
    valor_celsius = float(input("valor celsius: "))
    calculo_conversao = (valor_celsius * 9 / 5 ) + 32
    print(calculo_conversao)
except ValueError:
    print("você não inseriu um número")    

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
frase = input("coloque a frase ou palavra: ")
if isinstance(frase, str):
    frase_inversa = frase[::-1]
    if frase == frase_inversa:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
else:
    print("Coloque um texto")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
try:
    numero1 = float(input("numero 1: "))
    operador = input("operador: ")
    numero2 = float(input("numero 2: "))

    if operador == "+":
        calculo = numero1 + numero2
    elif operador == "-":
        calculo = numero1 - numero2
    elif operador == "/":
        calculo = numero1 / numero2
    elif operador == "*":
        calculo = numero1 * numero2
    else:
        print("Operador invalido")
    print(calculo)
except ValueError:
    print("Tipo de dado errado")



# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    numero1 = float(input("numero 1: "))
    if isinstance(numero1, float) or isinstance(numero1, float):
        if numero1 > 0:
            print("número é positivo")
        elif numero1 < 0:
            print("número é negativo")
        elif numero1 == 0:
            print("O número é nulo")
        else:
            print("Não é número")

    verifica_par = numero1 % 2
    if verifica_par == 0:
        print("O número é par")
    else:
        print("É ímpar")

except:
    print("Tipo de dado inserido está errado")       

