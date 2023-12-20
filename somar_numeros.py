def somar_numeros(*args):
    soma = sum(args)
    return soma

numeros = []
while True:
    try:
        numero = int(input("Digite um número (ou -1 para parar): "))
        if numero == -1:
            break
        numeros.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")

resultado = somar_numeros(*numeros)
print(f"A soma dos números inseridos é: {resultado}")
