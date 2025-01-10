# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f'{self.ano} {self.marca} {self.modelo}'

    def buzinar(self):
        return 'Buzina: Beep Beep!'

# Criando um objeto da classe Carro
meu_carro = Carro('Toyota', 'Corolla', 2020)

# Usando os métodos do objeto
print(meu_carro.descricao())  # Saída: 2020 Toyota Corolla
print(meu_carro.buzinar())    # Saída: Buzina: Beep Beep!
