#Contador decrescente

def contador (cont):
    while cont > 0:
        print (cont)
        cont = cont - 1

numero = int (input ('Digite qualquer número: '))
contador(numero)