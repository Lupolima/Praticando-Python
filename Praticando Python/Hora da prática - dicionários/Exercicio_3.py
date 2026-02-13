# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

numeros = {"1": 1, "2": 4, "3": 9, "4": 16, "5": 25}
print(numeros)

''' Ou poderia ser assim

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
'''