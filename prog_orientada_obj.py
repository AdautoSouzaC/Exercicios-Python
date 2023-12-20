


class Clientes:
    def __init__(self, razao_social=None,cnpj=None, endereco = None):
        self.razao_social = (None)
        self.cnpj = (None)
        self.endereco = (None)

    def cadastrar_cliente(self, cadastrar_clien):
    
        self.razao_social = input("Digite a razão social:")
        self.cnpj = int(input("Digite o cnpj :"))
        self.endereco = input("Digite o endereço do cliente:")

    def mostrar_dados(self):
       print("----Cliente cadastro---")
       print(f"razão social {self.razao_social}")
       print(f"cnpj {self.cnpj}")
       print(f"Endereço {self.endereco}")

clie1= Clientes() #cria objeto
clie1.cadastrar_cliente()
clie1.mostrar_dados()
