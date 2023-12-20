#Funções e Pacotes

'''def boas_vindas():
    nome=input("Digite um nome:")
    print("Seja bem vindom {nome}")

boas_vindas() #chamada da função'''

#Parametros

def mostras_dados_usuario(nome,idade,cpf,endereco):
    print(f"Seja bem vindo(a) {nome}!")
    print(f"Idade {idade}")
    print(f"Cpf {cpf}")
    print(f"Endereço {endereco}")
nome = input("Digite seu nome: ")
idade =input("Digite sua idade: ")
cpf = input("Digite seu cpf: ")
endereco = input("Digite seu endereço: " )
return nome,idade,cpf, endereco

#mostras_dados_usuario(nome,idade,cpf,endereco) #chamada da função

#Escopo de variavel

'''def exemplo(nome):# ESCOPO GLOBAL
    global sobrenomenome #DEFINIÇÃO GLOBAL
    nome = "Cris"
    print(f"entrou na função:{nome}")


nome = "Dauto"#DEFINIÇÃO GLOBAL
sobrenome ="souza"#DEFINIÇÃO GLOBAL
print("Antes da funão:", nome, sobrenome)
exemplo(nome)
print("Depois da função:", nome, sobrenome)'''

#EXEMPLO DE CHAMADA DE FUNÇÕES

'''def bom_dia():
    print("bom dia")

def boa_tarde():
    print("boa tarde")

def boa_noite():
    print("boa noite")

boa_noite()''''''

