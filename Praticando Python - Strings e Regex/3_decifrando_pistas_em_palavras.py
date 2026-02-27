'''
Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. Sua missão é desenvolver um programa que extraia trechos importantes de qualquer palavra digitada.

Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.

Exemplo de Entrada:
Digite a palavra-chave: Misterioso

Saída esperada:
Primeiras: Mis
Últimas: oso

'''

palavra = input("Digite uma palavra-chave: ")
#primeiras = palavra[0:3]
#ultimas = palavra[-3:]
print(f"Primeiras: {palavra[0:3]}")
print(f"Últimas: {palavra[-3:]}")