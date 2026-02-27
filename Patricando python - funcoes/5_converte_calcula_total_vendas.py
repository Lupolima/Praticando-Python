'''
Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

Exemplo de entrada:
Digite os valores das vendas: 100 250 300 

Saída esperada:
O total de vendas foi: 650 
'''

# Define a função que recebe a string com todos os valores
def calcula_vendas(valores):
    # Divide a string em uma lista de strings, usando o espaço como separador
    listas = valores.split()
    # Inicializa a variável que vai guardar a soma dos valores
    total = 0
    # Inicia um laço para percorrer cada elemento da lista gerada pelo split
    for lista in listas:
        # Converte o elemento atual (que é texto) para número decimal (float)
        lista = float(lista)
        # Adiciona o valor convertido ao montante acumulado no total
        total += lista
    # Retorna o valor final da soma para quem chamou a função
    return total

# {action_respond_info} Captura a entrada do usuário como uma única string
valores = input("Digite os valores das vendas separado por espaço: ")
# {action_respond_info} Chama a função e exibe o resultado formatado na tela
print(f"O total de vendas foi: {calcula_vendas(valores)}")

'''
UM JEITO MAIS DIRETO DE FAZER

# {action_respond_info} O input recebe o texto e o .split() já o transforma em uma lista de strings
valores = input("Digite os valores das vendas: ").split() 

# O map(float, valores) aplica a função float em cada item da lista individualmente
# O sum() pega todos esses números convertidos e realiza a soma total
total = sum(map(float, valores)) 

# {action_respond_info} Exibe o resultado final utilizando uma f-string
print(f"O total de vendas foi: {total}")
'''