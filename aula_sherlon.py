#print("olá mundo!")

total = 0.0 #valor a ser pago
while True: 
    print("1) Cadastrar novo produto, 2) Desconto, 0) Finalizar") 
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        print("Programa Finalizado! ")
        break #Finaliza um loop
        
    elif opcao == 1:
        preco_produto = float(input("Digite o preço do produto: "))
        total += preco_produto
        print(f"Valor parcial: {total}")
    elif opcao == 2:
        desconto = float(input("Digite o desconto: "))
        total -= desconto
        print(f"Valor parcial: {total}")
    else:
        print("opção invalida!")
        
print(f"Valor total: {total}")