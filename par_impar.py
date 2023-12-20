def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = par_impar(numero)
    print(f"O número {numero} é {resultado}")

if __name__ == "__main__":
    main()
