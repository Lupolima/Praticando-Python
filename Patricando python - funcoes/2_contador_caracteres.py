'''
Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

Exemplo de entrada:
Digite uma palavra: tecnologia 

Saída esperada:
Essa palavra tem 10 caracteres. 
'''
'''def calcula_caractere(palavra):
    numero = 0
    for letras in palavra:
        numero += 1
    return numero

palavra = input("Digite uma palavra: ")
quantidade = calcula_caractere(palavra)
print(f"Essa palavra tem {quantidade} caracteres")
'''

def calcula_caractere(palavra):
    return len(palavra)

texto = input("Digite uma palavra: ")
print(f"Essa palavra tem {calcula_caractere(texto)} caracteres")