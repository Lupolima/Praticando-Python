class Restaurante:
    restaurantes = []
    contador = 0

    # Atributos de Classe (ou Variáveis de Classe) = restaurantes = []
    # Atributos de Instância (ou Variáveis de Instância) = self.nome, self.categoria...
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        Restaurante.contador += 1
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'ATIVO' if self._ativo else 'INATIVO'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.listar_restaurantes()
#print(f'\nTotal de Restaurantes: {Restaurante.contador}')
print(f'\nTotal de Restaurantes: {len(Restaurante.restaurantes)}')