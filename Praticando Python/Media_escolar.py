# Autor: Handel Mercês
notas = []
for i in range(1, 5):
    nota = int(input(f"Digite a nota {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
situacao = "Aprovado" if media >= 7 else "Reprovado"

print(f"Sua média é: {media}")
print(f"O aluno foi: {situacao}")

    