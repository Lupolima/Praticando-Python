idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
    print("Você é uma criança\n")
elif 13 <= idade <= 18:
    print("Você é um Adolescente\n")
elif idade >= 18:
    print("Você é um Adulto\n")
else:
    print("Numero inválido\n")