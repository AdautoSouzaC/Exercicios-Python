
#contar letras
def contar_letra(frase, letra):
    contador = 0
    for char in frase:
        if char == letra:
            contador += 1
    return contador

letra_desejada = input("Digite a letra desejada: ")
frase = input("Digite a frase: ")

# Converte tudo para minúsculas para tornar a comparação case-insensitive
letra_desejada = letra_desejada.lower()
frase = frase.lower()

# Chama a função para contar a letra na frase
quantidade = contar_letra(frase, letra_desejada)

print(f"A letra '{letra_desejada}' aparece {quantidade} vezes na frase.")
