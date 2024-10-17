print("Bem-vindo à Máquina de Venda Automática de Ingressos de Cinema!")
nome = input("Por favor, digite seu nome: ")

# Verifica a disponibilidade de ingressos
quantidade_ingressos = 10  # Suponha que haja 10 ingressos disponíveis

# Verifica se há ingressos disponíveis
if quantidade_ingressos > 0:
    print("Ingressos estão disponíveis!")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")
    exit()  # Encerra o programa se não houver ingressos

# Pergunta ao cliente se ele deseja comprar um ingresso
comprar = input("Deseja comprar um ingresso? (Sim/Não): ")

# Verifica a resposta do cliente
if comprar.lower() == "sim":
    idade = int(input("Digite sua idade: "))
    
    # Recomenda filmes com base na idade
    if idade < 12:
        filmes = ["Frozen", "A Fantastica Fabrica de Chocolate", "Moana"]
    elif 12 <= idade < 18:
        filmes = ["Vingadores Guerra infinita", "Vingadores Ultimato", "Homem Aranha", "World War Z"]
    else:
        filmes = ["Star Wars", "American Pie", "The Boys"]
    
    print("Filmes disponíveis para sua idade:")
    for i, filme in enumerate(filmes, 1):
        print(f"{i}. {filme}")
    
    # Pergunta ao cliente qual filme ele deseja assistir
    escolha = int(input("Escolha o número do filme que deseja assistir: "))
    
    if 1 <= escolha <= len(filmes):
        filme_escolhido = filmes[escolha - 1]
        quantidade_ingressos -= 1  # Diminui a quantidade de ingressos
        print(f"Ingresso para '{filme_escolhido}' comprado com sucesso!")
        if quantidade_ingressos == 0:
            print("Todos os ingressos estão esgotados!")
    else:
        print("Escolha inválida.")
else:
    print("Obrigado por visitar a Máquina de Venda Automática de Ingressos de Cinema!")

# Exibe a quantidade de ingressos restantes
print(f"Quantidade de ingressos restantes: {quantidade_ingressos}")