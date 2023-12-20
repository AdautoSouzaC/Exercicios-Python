#verificar True e False

def verifica_prefixo(primeira_palavra, segunda_palavra):
    if primeira_palavra.startswith(segunda_palavra):
        return True
    else:
        return False

# Solicita as palavras ao usuário
primeira_palavra = input("Digite uma palavra: ")
segunda_palavra = input("Digite a segunda palavra: ")

# Chama a função e imprime o resultado
resultado = verifica_prefixo(primeira_palavra, segunda_palavra)

print(resultado)
