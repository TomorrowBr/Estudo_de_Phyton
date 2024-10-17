import random
import string

# Lista de nomes dos clientes
clientes = [
    "Alan Lopes",
    "Alex Santos Gomes",
    "Alexa Adriely Martins Dos Santos",
    "Ana Paula Souza",
    "Antonio Augusto",
    "Arthur Dias Dos Santos",
    "Bernado Santos",
    "Carlos Eduardo Gresik",
    "Damires Davora",
    "Danillo Freitas Matos",
    "Edson Nunes",
    "Eduardo Soares Silva Neto",
    "Emilly Kessia",
    "Emily Celes Barroso",
    "Enderigo De Carvalho",
    "Erik Galvao Paranhos Da Silva",
    "Fabiola Dantas Rocha Araujo De Almeida",
    "Gabriel Bom Furlan",
    "Gustavo Kouzo Assef",
    "Gustavo Nunes De Almeida",
    "João Cleber Neves Nascimento",
    "Joao Victor Santos Soares",
    "João Yuri",
    "Joaquin Pereira Da Silva Neto",
    "Juam Lima Santos",
    "Landra Costa",
    "Larissa Bispode Matos",
    "Lucas Amaral",
    "Lucas Goes",
    "Luis Fernando Leal Gomes",
    "Luiz Guilherme",
    "Marcelo Pessoa Santos",
    "Marcio Santos",
    "Marcos Bezerra Lima",
    "Maria Eduarda Lessa",
    "Matheus Ramos",
    "Miguel Afonco Marques",
    "Miguel Fonseca Muniz",
    "Pablo Conceicao Menezes",
    "Paolla Pontes",
    "Paulo Ricardo",
    "Pedro Antonio Menezes Rios",
    "Rayane Alves Dos Santos",
    "Robervan Dos Santos Oliveira",
    "Rodrigo Augusto Santini",
    "Romulo Lino",
    "Rosangela Cidreira De Jesus",
    "Samuel Pereira Dos Santos",
    "Sergio Ricardo Freitas",
    "Soanne Cristino Almeida Dos Santos",
    "Taiana Carvalho",
    "Tainan Moreira",
    "Tarcisio Da Silva Gomes",
    "Vera Lucia Leite",
    "Vicente Do Valle",
    "Vinicius Gabriel Oliveira",
    "Zenon Moreira Gomes Junior"
]

# Lista de números de telefone dos clientes (correspondente à lista de clientes)
telefones = [
    "(73)98848-7061",
    "(73)98808-7182",
    "(73)99823-1337",
    "(73)99983-1309",
    "(73)99144-4472",
    "(73)98205-3540",
    "(73)9981-5644",
    "(73)9914-7547",
    "(73)99145-0082",
    "(73)98833-0365",
    "(73)99133-6486",
    "(73)98179-6224",
    "(73)98122-8930",
    "(73)98887-1423",
    "(73)99983-1252",
    "(73)99115-5151",
    "(73)98847-2266",
    "(73)98875-6672",
    "(73)99983-4889",
    "(73)98219-8814",
    "(73)99150-0893",
    "(73)98861-3886",
    "(73)99957-9892",
    "(73)98251-8875",
    "(73)98887-2878",
    "(11)96205-8518",
    "(73)98816-4888",
    "(73)99105-5529",
    "(73)99133-0046",
    "(73)99119-9182",
    "(73)99183-5428",
    "(77)99822-1012",
    "(73)99120-0506",
    "(73)99167-0738",
    "(73)9914-0510",
    "(73)99158-2044",
    "(73)99983-4068",
    "(73)98108-2269",
    "(73)98871-4320",
    "(71)98344-7171",
    "(73)98894-1815",
    "(73)98242-4970",
    "(73)98889-0968",
    "(73)99962-8090",
    "(73)99100-0210",
    "(73)98124-4588",
    "(73)98843-2180",
    "(73)9967-3234",
    "(73)99998-7748",
    "(73)99983-7734",
    "(73)98804-1639",
    "(73)98122-9469",
    "(73)98247-4236",
    "(73)99133-1616",
    "(73)99181-8180",
    "(73)98111-1717",
    "(73)99909-1999"
]

# Mensagem base com espaço reservado para o nome do cliente e o cupom
mensagem_base = """
🎉 *Parabéns, {nome}* 🎉

Esse é um Mês especial, e nós da DirksenPlay queremos desejar muita alegria, saúde e sucesso! Como forma de agradecimento por fazer parte da nossa história, estamos te presenteando com um *cupom de R$ 10,00* para usar na próxima vez que aparecer no quiosque para jogar conosco! 🛍️

*Cupom:* {cupom}
*Válido até:* 31/10/2024

Esperamos que esse pequeno gesto torne seu dia ainda mais especial! 🎁

Com carinho,  
Dirksen Play
"""

# Função para gerar um cupom aleatório de 10 dígitos
def gerar_cupom():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=10))

# Função para formatar o número de telefone para o formato internacional
def formatar_telefone(telefone):
    return telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

# Iterar sobre a lista de clientes e gerar o link do WhatsApp para cada mensagem personalizada
for cliente, telefone in zip(clientes, telefones):
    cupom = gerar_cupom()
    mensagem_personalizada = mensagem_base.format(nome=cliente, cupom=cupom)
    telefone_formatado = formatar_telefone(telefone)
    link_whatsapp = f"https://wa.me/{telefone_formatado}?text={mensagem_personalizada}"
    print(f"Link para {cliente}: {link_whatsapp}")
    print("-" * 80)  # Separador entre mensagens