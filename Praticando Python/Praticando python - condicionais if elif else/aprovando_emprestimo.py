'''Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

    O valor da renda mensal precisa ser maior que R$ 2.000,00.
    O valor da parcela não pode ultrapassar 30% da renda.

Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

Saída esperada:
Digite o valor da sua renda mensal: 2500
Digite o valor da parcela desejada: 800
Empréstimo negado: parcela acima de 30% da renda.
'''

renda = float(input("Digite o valor da sua renda: "))
parcela = float(input("Digite o valor da parcela desejada: "))
if parcela > (renda * 0.3):
    print("Empréstimo NEGADO: A parcela está acima de 30% da renda")
elif renda <= 2000:
    print("Empréstimo NEGADO: renda insuficiente.")
else:
    print("Emprestimo AUTORIZADO!")