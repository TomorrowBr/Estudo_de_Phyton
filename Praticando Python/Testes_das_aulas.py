texto = "Explorando a diversidade da liguagem de programação com Python."

print(f"Tamanho do texto: = {len(texto)}")
print(f"Texto em maiúsculas: = {texto.upper()}")
print(f"Python in texto: = {'Python' in texto}")
print(f"Quantidade de 'a' no texto: = {texto.count('a')}")    
print(f"As primeiras 10 letras do texto: = {texto[:10]}")
print(f"As últimas 10 letras do texto: = {texto[-10:]}")
print(f"Texto invertido: = {texto[::-1]}")

cores = ["vermelho", "verde", "azul", "amarelo", "roxo", "preto", "branco", "cinza", "laranja", "rosa"]
for cor in cores:
    print(f"posição: {cores.index(cor)}, cor: {cor}")


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