'''
Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

Exemplo de entrada:
Digite os números separados por espaço: 1 2 3 4 5 6 

Saída esperada:
Números pares: 2 4 6 
'''

# {action_respond_info} Recebe a entrada do usuário e cria uma lista de strings (ex: ['1', '2', '3'])
lista = input("Digite os números separados por espaço: ").split()
# O filter cria um objeto que "peneira" a lista original
# A função lambda converte cada x em inteiro para testar se é par (resto da divisão por 2 igual a zero)
pares = filter(lambda x: int(x) % 2 == 0, lista)
# {action_respond_info} O join percorre o objeto 'pares', unindo os elementos com um espaço entre eles
# Como os itens dentro de 'pares' ainda são as strings originais da 'lista', o join funciona sem erro
print(f"Números pares: {' '.join(pares)}")

'''
# {action_respond_info} Recebe a entrada do usuário e já cria a lista de strings
lista = input("Digite os números separados por espaço: ").split()

# {action_respond_info} O join recebe diretamente o resultado do filter.
# O Python processa o filtro e já vai entregando os itens para o join "colar" com espaços.
print(f"Numeros Pares: {' '.join(filter(lambda x: int(x) % 2 == 0, lista))}")
'''