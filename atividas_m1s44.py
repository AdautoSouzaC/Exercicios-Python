#cadastro clientes banco

while True:
  print("1) Cadastrar cliente, 2) Deletar cliente, 3) Mostrar clientes, 0) Sair")
  opcao = int(input("Digite a opção desejada: "))
  if opcao == 0:
    print("Programa finalizado!")
    break
  elif opcao == 1:

    cliente = {}
    cliente["Nome"] = input("Qual o nome dp cliente:")
    cliente["CPF"] = input("Digite seu cpf:")
    cliente["Idade"] = int(input("Qual a sua idade:"))

