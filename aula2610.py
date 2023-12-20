#texto = "olá familia da Cristiane e do Adauto"
#print(texto[0:6])

'''familia = "Adauto Cristiane Giovanna Enzo Davi"
tamanho = len(familia)
print (len(familia))

for i in range(tamanho):
    print(i,familia[i])'''

'''clientes = ['Adauto', 'Cristiane', 'Giovanna', 'Enzo', 'Davi', 'Carly', 'Bonnie', 'Aika']
print(clientes)
tamaho=len(clientes)
print(f"Exitem {tamaho} clientes cadastrados no sistema")
for i in range(tamaho):
    print(i, clientes[i]) '''

estoque = []
while True:
    print("1)cadastrar produto,2)Mostrar estoque, 0)sair")
    opção = int(input("digite a opção desejada:"))
    if opção==0:
        print("Siatema finalizado")
        break
    elif opção== 1:
        material = input("Informe o produto que deseja cadastrar:")
        estoque.append(estoque)
    elif opção== 2:
        print(f'o estoque contem{len(estoque)} produtos')
        print('Saldo', estoque)
    else:
        print("Opção invalida.")