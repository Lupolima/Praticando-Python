class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Bohemian Rhapsody', artista='Queen', duracao='5:55')
musica2 = Musica(nome='Imagine', artista='John Lennon', duracao='3:03')
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao='6:30')

musicas = [musica1, musica2, musica3]

for musica in musicas:
    print(f'{musica.nome} - {musica.artista} - {musica.duracao}')


