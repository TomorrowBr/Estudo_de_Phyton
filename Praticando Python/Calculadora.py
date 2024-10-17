def adicao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 + n2

def subtracao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 - n2

def multiplicacao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 * n2

def divisao():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    return n1 / n2

def potenciacao():
    n1 = int(input("Digite o número:"))
    n2 = int(input("Digite a potência:"))
    return n1 ** n2

def raiz_quadrada():
    n1 = int(input("Digite o número:"))
    return n1 ** 0.5

while True:
    print("\nBem vindo a minha calculadora em Python")
    print("Escolha a operação que deseja realizar:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("6 - Raiz Quadrada")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada:"))

    if opcao == 0:
        print("Obrigado por usar a minha calculadora em Python")
        break
    elif opcao < 1 or opcao > 6:
        print("Opção inválida")
    else:
        if opcao == 1:
            print("Você escolheu a opção de adição")
            print(f"O resultado da adição é: {adicao()}")
        elif opcao == 2:
            print("Você escolheu a opção de subtração")
            print(f"O resultado da subtração é: {subtracao()}")
        elif opcao == 3:
            print("Você escolheu a opção de multiplicação")
            print(f"O resultado da multiplicação é: {multiplicacao()}")
        elif opcao == 4:
            print("Você escolheu a opção de divisão")
            print(f"O resultado da divisão é: {divisao()}")
        elif opcao == 5:
            print("Você escolheu a opção de potenciação")
            print(f"O resultado da potenciação é: {potenciacao()}")
        elif opcao == 6:
            print("Você escolheu a opção de raiz quadrada")
            print(f"A raiz quadrada do número é: {raiz_quadrada()}")