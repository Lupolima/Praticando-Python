class Musica:
    nome = ""
    artista = ""
    duracao = ""

musica1 = Musica()
musica1.nome = "Bohemian Rhapsody"
musica1.artista = "Queen"
musica1.duracao = "5:55"

musica2 = Musica()
musica2.nome = "Imagine"
musica2.artista = "John Lennon"
musica2.duracao = "3:03"

musica3 = Musica()
musica3.nome = "Hotel California"
musica3.artista = "Eagles"
musica3.duracao = "6:30"

print(musica1.nome, "-", musica1.artista, "-", musica1.duracao)
print(f"{musica2.nome} - {musica2.artista} - {musica2.duracao}")
print(musica3.nome, musica3.artista, musica3.duracao)

