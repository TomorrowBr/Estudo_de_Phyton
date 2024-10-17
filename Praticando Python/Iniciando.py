nome = input("Digite seu nome: ")
print (nome,"bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world")    

# Operadores de comparação

1 == 1  # Verifica se 1 é igual a 1. Resultado: True
4 > 2   # Verifica se 4 é maior que 2. Resultado: True
2 < 3   # Verifica se 2 é menor que 3. Resultado: True
1 >= 1  # Verifica se 1 é maior ou igual a 1. Resultado: True
1 <= 2  # Verifica se 1 é menor ou igual a 2. Resultado: True
4 != 5  # Verifica se 4 é diferente de 5. Resultado: 

int  # Resultado: 1
float  # Resultado: 1.0

# Operadores aritméticos

1 + 1   # Adição. Resultado: 2
2 - 1   # Subtração. Resultado: 1
2 * 2   # Multiplicação. Resultado: 4
4 / 2   # Divisão. Resultado: 2
4 % 3   # Módulo. Resultado: 1
2 ** 3  # Exponenciação. Resultado: 8
3 // 2  # Divisão inteira. Resultado 1

# Operadores de atribuição

x = 1   # Atribui o valor 1 à variável x
x += 1  # Adiciona 1 ao valor de x
x -= 1  # Subtrai 1 do valor de x
x *= 2  # Multiplica o valor de x por 2
x /= 2  # Divide o valor de x por 2
x %= 2  # Atribui a x o módulo do valor atual de x por 2
x **= 2 # Atribui a x o valor de x elevado à potência de 2
x //= 2 # Atribui a x o valor da divisão inteira de x por 2

# and - Operador lógico E
#  or - Operador lógico OU
# not - Operador lógico NÃO
# Operadores lógicos

True and True   # Verifica se True e True são verdadeiros. Resultado: True
True and False  # Verifica se True e False são verdadeiros. Resultado: False
False and False # Verifica se False e False são verdadeiros. Resultado: False


# Exemplo de uso do in
if 1 in [1, 2, 3]:
    print("1 está na lista")

# Exemplo de uso do for
for i in range(1, 5):
    print(i)

# Exemplo de uso do while
i = 1
while i < 5:
    print(i)
    i += 1

# Exemplo de uso do break
for i in range(1, 5):
    if i == 3:
        break
    print(i)

# Exemplo de uso do continue
for i in range(1, 5):
    if i == 3:
        continue
    print(i)

# Exemplo de uso do range
for i in range(1, 5):
    print(i)

# Exemplo de uso do range com incremento
for i in range(1, 5, 2):
    print(i)

# Exemplo de uso do range com decremento
for i in range(5, 1, -1):
    print(i)

#Funções 
#Funções são blocos de código que são executados quando chamados.
#Funções são definidas usando a palavra-chave def.
#As funções podem ter parâmetros que são passados quando a função é chamada.
#As funções podem retornar um valor usando a palavra-chave return.

# range - Gera uma sequência de números 
# for - Loop 
# while - Usado para executar um bloco de código repetidamente enquanto uma condição especificada é verdadeira
# break - Termina o loop
# continue - Pula a iteração atual e continua com a próxima
# in - Verifica se um valor está presente em uma sequência
# i - Variável de controle do loop
# f - String de formatação f-strings  (f"Olá, {nome}!")     

# print(): Imprime a saída no console
print("Hello, world!") 

# input(): Lê a entrada do usuário
nome = input("Digite seu nome: ") 

# int(): Converte um valor para inteiro
numero = int("10")  # 10

# float(): Converte um valor para ponto flutuante
numero = float("10.5") # 10.5

# str(): Converte um valor para string
texto = str(10) # "10"

# len(): Retorna o comprimento de um objeto
tamanho = len("Hello, word!")  # 12

# range(): Gera uma sequência de números
numeros = range(1, 5) # [1, 2, 3, 4]

# type(): Retorna o tipo de um objeto
tipo = type(10) # int

# abs(): Retorna o valor absoluto de um número
valor = abs(-10) # 10

# round(): Arredonda um número
numero = round(10.5) # 11

# bool(): Converte um valor para booleano
booleano = bool(1) # True
booleano = bool(0) # False

# list(): Converte um objeto para uma lista
lista = list((1, 2, 3)) # [1, 2, 3]

# tuple(): Converte um objeto para uma tupla
tupla = tuple([1, 2, 3]) # (1, 2, 3)    

# dict(): Cria um dicionário
dicionario = dict(nome="João", idade=30) # {"nome": "João", "idade": 30}

# set(): Cria um conjunto
conjunto = set([1, 2, 3]) # {1, 2, 3}

# max(): Retorna o maior valor de um iterável
maximo = max([1, 2, 3]) # 3

# min(): Retorna o menor valor de um iterável  
minimo = min([1, 2, 3]) # 1 

# sum(): Retorna a soma de um iterável
soma = sum([1, 2, 3]) # 6

# zip(): Combina duas listas em uma lista de tuplas
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
combinacao = zip(lista1, lista2) # [(1, "a"), (2, "b"), (3, "c")]

# all(): Retorna True se todos os elementos de um iterável são verdadeiros
todos = all([True, True, True]) # True

# any(): Retorna True se algum dos elementos de um iterável é verdadeiro
algum = any([True, False, False]) # True

# sorted(): Retorna uma lista ordenada
ordenado = sorted([3, 1, 2]) # [1, 2, 3]

# reversed(): Retorna um iterável reverso
reverso = reversed([1, 2, 3]) # [3, 2, 1]

# map(): Aplica uma função a todos os elementos de um iterável
def dobro(x):
    return x * 2
resultado = map(dobro, [1, 2, 3]) # [2, 4, 6]

# filter(): Filtra os elementos de um iterável com base em uma função
def par(x):
    return x % 2 == 0
resultado = filter(par, [1, 2, 3, 4]) # [2, 4]

# def: Define uma função
def saudacao(nome):
    return f"Olá, {nome}!"
mensagem = saudacao("João") # "Olá, João!"

# return: Retorna um valor de uma função
def soma(a, b):
    return a + b  
resultado = soma(1, 2) # 3

# for: Loop que itera sobre um iterável
for i in range(1, 5):
    print(i) # 1, 2, 3, 4

# while: Loop que executa um bloco de código enquanto uma condição é verdadeira
i = 1
while i < 5:
    print(i)
    i += 1 # 1, 2, 3, 4

# if: Executa um bloco de código se uma condição é verdadeira
if 1 == 1:
    print("Verdadeiro") # Verdadeiro
    
# else: Executa um bloco de código se a condição do if for falsa
if 1 == 2:
    print("Verdadeiro")
else:
    print("Falso") # Falso

# elif: Executa um bloco de código se a condição do if for falsa e a condição do elif for verdadeira
if 1 == 2:
    print("1")
elif 1 == 1:
    print("2")
else:
    print("3") 

# append(): Adiciona um elemento ao final de uma lista
lista = [1, 2, 3]
lista.append(4) # [1, 2, 3, 4]

# insert(): Adiciona um elemento em uma posição específica de uma lista
lista = [1, 2, 3]
lista.insert(1, 4) # [1, 4, 2, 3]

# remove(): Remove o primeiro elemento com um valor específico de uma lista
lista = [1, 2, 3]
lista.remove(2) # [1, 3]

# pop(): Remove um elemento em uma posição específica de uma lista e retorna o elemento removido
lista = [1, 2, 3]
elemento = lista.pop(1) # [1, 3], elemento = 2

texto = "Explorando a diversidade da liguagem de programação com Python."
print(f"Tamanho do texto: = {len(texto)}")
print(f"Texto em maiúsculas: = {texto.upper()}")
print(f"Python in texto: = {'Python' in texto}")
print(f"Quantidade de 'a' no texto: = {texto.count('a')}")    
print(f"As primeiras 10 letras do texto: = {texto[:10]}")
print(f"As últimas 10 letras do texto: = {texto[-10:]}")
print(f"Texto invertido: = {texto[::-1]}")

def adicao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 + n2
print(f"O resultado da adição é: {adicao()}")

def subtracao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 - n2
print(f"O resultado da subtração é: {subtracao()}")

def multiplicacao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 * n2
print(f"O resultado da multiplicação é: {multiplicacao()}")

def divisao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 / n2
print(f"O resultado da divisão é: {divisao()}")

def potenciacao():
    n1 = int(input("Digite o número:"))
    n2 = int(input("Digite a potência:"))
    return n1 ** n2
print(f"O resultado da potenciação é: {potenciacao()}")

def raiz_quadrada():
    n1 = int(input("Digite o número:"))
    return n1 ** 0.5
print(f"A raiz quadrada do número é: {raiz_quadrada()}")