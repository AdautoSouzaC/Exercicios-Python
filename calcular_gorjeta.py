#calcular gorjeta

def calcular_gorjeta(valor_conta, taxa_servico):
    gorjeta = (valor_conta * taxa_servico) / 100
    return gorjeta

# Informar valores da operação

valor_conta = float(input("Valor final da conta? R$: "))
taxa_servico = int(input(" Qual o percentual da taxa de serviço? %: "))

#calculando gorjeta
gorjeta_calculada = calcular_gorjeta(valor_conta, taxa_servico)

#Resultado final com duas casas decimais
print(f"A gorjeta do garçom é de R$: {gorjeta_calculada:.2f}")
