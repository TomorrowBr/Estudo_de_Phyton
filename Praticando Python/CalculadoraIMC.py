nome = input ("Digite seu nome: ")

peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc < 24.9:
    situacao = "Peso normal"
elif imc < 29.9:
    situacao = "Sobrepeso"
elif imc < 34.9:
    situacao = "Obesidade Grau 1"
elif imc < 39.9:
    situacao = "Obesidade Grau 2"
else:
    situacao = "Obesidade Grau 3"

print("A Situação do seu IMC é:", situacao)

print("Obrigado por usar nosso programa", nome)

print("Fim do programa")