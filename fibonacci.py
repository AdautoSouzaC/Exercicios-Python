class Fibonacci:

    def __init__(self,maximo):

        self.elemento_atual = 0
        self.proximo_elemento = 1
        self.maximo = maximo

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.elemento_atual > self.maximo:
            raise StopIteration
        
        valor_retorno = self.elemento_atual 

        self.elemento_atual = self.proximo_elemento
        self.proximo_elementeo = valor_retorno + self.proximo_elemento

        return valor_retorno
    
    def __str__(self):
        return f'Fibonacci de {self.maximo}'
    
obj_Fibonacci = Fibonacci(10)
print(obj_Fibonacci)
for numero in obj_Fibonacci:
    print(numero)
    
    


        
