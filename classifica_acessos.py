# minha abordagem inicial foi
# 1. separa 90% para treino e 10% para teste:88.88888888888889%

from dados import carregar_acessos

(X,Y) = carregar_acessos()

treino_dados = X[:90]

treino_marcacoes = Y[:90]

teste_dados = X[-9:]

teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes

acertos = [ diferenca for diferenca in diferencas if diferenca == 0 ]

total_de_acertos = len(acertos)

total_de_elementos = len(teste_dados)

taxa_acerto = 100. * total_de_acertos / total_de_elementos

print('Taxa de Acertos:', taxa_acerto,'%')