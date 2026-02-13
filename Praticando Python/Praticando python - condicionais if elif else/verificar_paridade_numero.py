'''Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

Saída esperada:
Digite um numero inteiro: 20
0 numero é par.
'''

numero = int(input("Digite um numero inteiro: "))
if numero % 2 == 0:
    print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é impar.")