class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")
        print("Saaai da frente...")
        print("Tôoooo passando...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.itens()]}"


b1 = Bicicleta("vermelha","caloi",2022,600)
b1.buzinar()
b1.correr()
b1.parar()
print (b1.cor, b1.modelo, b1.ano, b1.valor)

