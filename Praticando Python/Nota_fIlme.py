# Lista de filme para classifcação

Filmes = ["Vingadores","Star Wars","Matrix","Senhor dos Anéis","Harry Potter","Jurassic Park","Indiana Jones","Piratas do Caribe","O Poderoso Chefão"]

#Mensagem de boas vindas

print("Bem vindo ao sistema de classificação de filmes")
print("Você tem 9 filmes para classicação")
print("Vamos começar")
print("Digite 0 a qualquer momento para parar.")

for filme in Filmes:
    #Solicitação da nota ao usuario
    classicacao = input(f"Como você classifica o filme {filme} de 1 a 5? (ou 0 para sair): ")

    #Verifica se o usuario deseja sair
    if classicacao == "0":
        print("Que pena que você não irá classificar mais os filmes")
        break

    classicacao = int(classicacao) 
    
    if classicacao < 1 or classicacao > 5:
     print("Por favor, digite uma nota válida")
    else:
     print(f"Você classificou o filme {filme} com {classicacao} estrelas")  
    
    
print("Obrigado por classificar os filmes")
    


   