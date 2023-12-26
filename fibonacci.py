class Fibonacci:

    def __init__(self,maximo):

        self.elemento_atual = 0
        self.proximo_elemento = 1
        self.maximo = maximo
        self.contagem = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contagem >= self.maximo:
            raise StopIteration
        
        valor_retorno = self.elemento_atual 

        self.elemento_atual = self.proximo_elemento
        self.proximo_elemento = valor_retorno + self.proximo_elemento
        self.contagem += 1
        return valor_retorno
    
    def __str__(self):
        return f'Fibonacci de {self.maximo}'
    
obj_Fibonacci = Fibonacci(20)
for i in range(25):
    try:
        print(obj_Fibonacci.__next__())
    except StopIteration:
        print("Excedeu o limite")
    
    


        
