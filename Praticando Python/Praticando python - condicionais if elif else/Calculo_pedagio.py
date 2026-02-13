'''Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

    Até 100 km: R$ 10,00
    Entre 100 km e 200 km: R$ 20,00
    Acima de 200 km: R$ 30,00

Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

Saída esperada:
Digite a distancia percorrida (em km): 250
Valor do pedagio: R$ 30,00

'''
distancia = float(input("Digite a distancia percorrida (em Km) "))
if distancia >= 100:
    valor = 10.00
elif 100 >= distancia >= 200:
    valor = 20.00
else:
    valor = 30.00
#muda os pontos para virgulas, assim ficara igual valor em reais.
valor = f"{valor:.2f}".replace('.', ',')
print(f"O valor do pedágio é: R$ {valor}")