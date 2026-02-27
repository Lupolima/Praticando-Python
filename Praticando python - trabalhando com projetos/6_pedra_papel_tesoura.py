'''
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

    Pedra ganha de Tesoura (Pedra quebra Tesoura);
    Tesoura ganha de Papel (Tesoura corta Papel);
    Papel ganha de Pedra (Papel cobre Pedra);
    Se ambos escolherem a mesma opção, é um empate.

Exemplo de entrada:
Escolha: pedra, papel ou tesoura? papel  

Saída esperada:
Computador escolheu: pedra
Você venceu!  

Caso o computador vença:
Computador escolheu: tesoura  
Você perdeu!  

Caso o computador escolha a mesma opção que você:
Computador escolheu: papel 
Empate!
'''
import random

escolha_user = input("Escolha: pedra, papel ou tesoura? ")
lista = ["pedra" "papel" "tesoura"]
escolha_pc = random.choice(lista)
if escolha_user == "pedra" and escolha_pc == "tesoura":
    print(f"Computador escolheu: {escolha_pc}")
    print("Você Venceu")