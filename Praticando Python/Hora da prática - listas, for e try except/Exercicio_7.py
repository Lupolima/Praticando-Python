'''
7. Construa um código que calcule a média dos valores em uma lista.
Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
'''



valores = input("Digite os valores separados por virgula: ").split(",")
soma = 0
try:
    for x in valores:
        if x:  # Verifica se a string não está vazia
            soma += int(x)
        else:
            print("Entrada inválida: Lista vazia")
            exit()  # Encerra o programa se encontrar uma string vazia
    media = soma / len(valores)
    print(f"A media dos valores é: {media} \n")
except ZeroDivisionError:
    print("Erro ao calcular a media, a lista está vazia")
except Exception as erro:
    print(f"Ocorreu um erro em: {erro}")