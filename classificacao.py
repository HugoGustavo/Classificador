# eh gordinho, tem perninnha curta, se faz auau
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# porco = 1
# cachorro = -1
marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [1, 1, 1]

misterioso2 = [1, 0, 0]

misterioso3 = [1, 0, 1]

testes = [misterioso1, misterioso2, misterioso3]

marcacoes_teste = [-1, 1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(dados, marcacoes)

resultado = modelo.predict(testes)

diferencas = resultado - marcacoes_teste

acertos = [ diferenca for diferenca in diferencas if diferenca == 0 ]

total_acertos = len(acertos)

total_de_elementos = len(testes)

taxa_de_acerto = 100. * total_acertos / total_de_elementos

print(taxa_de_acerto)