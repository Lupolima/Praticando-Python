'''2 - Utilizando o dicionário criado no item 1:

    Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    Adicione um campo de profissão para essa pessoa;
    Remova um item do dicionário.
'''

pessoa = [{"Nome":"José", "Idade":"20", "Cidade":"Palmas"} ]
pessoa["Idade"] = 21
pessoa["Profissão"] = ("Engenheiro")
del pessoa["Cidade"]