lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for numero in lista_de_numeros:
    if numero % 2 != 0:
        soma = soma + numero
print(soma)

'''
Poderia ser feito assim tambem:

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

A função range() aceita no máximo três argumentos: start, stop e step
range(1, 11, 2) gera uma sequência de números que começa em 1, vai até 10 (o 11 não é incluído)
e pula de 2 em 2. Assim, você itera diretamente sobre os números ímpares,
somando-os à variável soma_impares.

Outro exemplo da função range():
for impar in range(1, 11, 2):
        print(impar)

'''