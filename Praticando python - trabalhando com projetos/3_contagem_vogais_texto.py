'''
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

Exemplo de entrada:
Digite um texto: A linguagem Python é muito versátil.  

Saída esperada:
O texto contém 13 vogais.  

'''
def calculo_vogal(frase):
    vogais = "aeiou"
    contador = 0
    for letra in frase.lower():
        if letra in vogais:
            contador += 1
    return contador

frase = input("Digite um texto: ")
print(f"O texto contém {calculo_vogal(frase)} vogais.")