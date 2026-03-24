class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica('Bohemian Rhapsody', 'Queen', '5:55')
musica2 = Musica('Imagine', 'John Lennon', '3:03')
musica3 = Musica('Hotel California', 'Eagles', '6:30')

musicas = [musica1, musica2, musica3]

for musica in musicas:
    print(f'{musica.nome} - {musica.artista} - {musica.duracao}')


