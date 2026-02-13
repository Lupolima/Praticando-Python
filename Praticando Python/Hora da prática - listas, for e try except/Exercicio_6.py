lista = [1,2,3,4,5,6,7,8,9,10]
calculo = 0
try:
    for x in lista:
        calculo = calculo + x
    print(calculo)
except ValueError:
    print("Valor inserido é inválido")