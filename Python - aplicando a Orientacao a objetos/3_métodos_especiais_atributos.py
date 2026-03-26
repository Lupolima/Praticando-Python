'''
1.Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
2.Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
3.Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
4.Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
5.Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
'''

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} - {self.cor} - {self.ano}'

# Instanciando um carro e atribuindo valores aos seus atributos
gol = Carro('Gol', 'branco', '2012')

#print(gol.modelo, gol.ano, gol.cor)
print(gol)

class Restaurante:
    def __init__(self, nome, categoria, reserva, estacionamento, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.reserva = reserva
        self.estacionamento = estacionamento
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} - {self.categoria} - {self.reserva} - {self.estacionamento} - {self.ativo}'

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante1 = Restaurante('Jojo', 'Japonesa', 'sim', 'sim')

print(restaurante1)

class Cliente:
    def __init__(self, nome, idade, email, telefone):
            self.nome = nome
            self.idade = idade
            self.telefone = telefone
            self.email = email

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')