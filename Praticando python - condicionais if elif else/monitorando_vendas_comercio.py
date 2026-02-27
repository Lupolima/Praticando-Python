'''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

Saída esperada:
Digite a quantidade de macas vendidas: 15
Digite a quantidade de bananas vendidas: 3
As macas tiveram mais vendas.

'''

maca_vendida = input("Digite a quantidade de Maças vendidas: ")
banana_vendida = input("Digite a quantidade de Bananas vendidas: ")
if maca_vendida > banana_vendida:
    print("As maças tiveram mais vendas\n")
elif maca_vendida < banana_vendida:
    print("As bananas tiveram mais vendas\n")
else:
    print("As vendas de bananas e maças foram iguais\n")