'''

Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

Saída esperada:
Digite o total de despesas do més (R$): 5897.58
Atenção! Vocé ultrapassou o limite do orcamento.
'''

limite = 3000
despesa = float(input("Digite o total de despesas do més (R$): "))
if despesa > limite:
    print("Atenção! Vocé ultrapassou o limite do orcamento")
else:
    print("Você ainda está dentro do orçamento")