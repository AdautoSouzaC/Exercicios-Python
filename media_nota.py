nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media >= 7:
    print ('resultado: APROVADO')
    print("PARABÉNS")
elif (media >= 5):
    print("Resultado: VOCÊ ESTA DE RECUPERAÇÃO")
else:
    print('Resultado: REPROVADO')

print('sua média foi {}'.format(media))