'''
Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.

Crie um programa que junte as listas e exiba o resultado no formato produto: preço

Exemplo de entrada:
Digite os produtos separados por vírgula: maçã, banana, pera  

Digite os preços separados por vírgula: 2.5, 1.2, 3.0 

Saída esperada:
maçã: 2.5  

banana: 1.2  

pera: 3.0 
'''

produtos = input("igite os produtos separados por vírgula: ").split(",")
valores = input("Digite os preços separados por vírgula: ").split(",")

for p, v in zip(produtos, valores):
    print(f"{p.strip()}: {float(v.strip()):.2f}")
