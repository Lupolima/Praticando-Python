'''
Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes inseridos pelos clientes estejam no formato correto. O padrão esperado é que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). Para facilitar o trabalho, ela quer um programa que valide automaticamente os nomes fornecidos.

Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.

Exemplo de Entrada:
Digite o nome do cliente para validação: maria123

Saída esperada:
Nome inválido!

'''
import re

nome = input("Digite o nome do cliente para validação: ")
if re.fullmatch(r'[A-Z][a-z]*', nome):
    print("Nome válido!")
else:
    print("Nome inválido!")

'''
Em Python, o r no início de uma string indica que ela é uma "raw string". Isso significa que as barras invertidas (\) são tratadas como caracteres literais e não como caracteres de escape.

No contexto de expressões regulares (regex), usar raw strings é muito útil porque as regex frequentemente contêm barras invertidas. Se você não usar uma raw string, precisará escapar as barras invertidas, o que pode tornar a regex mais difícil de ler.

No início da string, você teria duas opções:

    Usar r'...' (raw string): Ideal para expressões regulares, pois evita problemas com caracteres de escape.
    Usar '...' (string normal): Nesse caso, você precisaria escapar as barras invertidas, o que pode tornar a regex mais complexa e difícil de entender.


r'': indica que é uma string raw, útil para expressões regulares.
[A-Z]: corresponde a qualquer letra maiúscula de A a Z.
[a-z]*: corresponde a zero ou mais letras minúsculas de a a z. O * significa "zero ou mais ocorrências" do padrão anterior. '''