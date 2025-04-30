# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

# Uma serie para somar 100 a cada linha (elemento) da coluna qtdePontos
# Uma série permite fazer operações com cada elemento dela com um valor (escalar)
df['qtdePontos'] + 100


# %%

# Mesma coisa do caso anterios, mas aumenta e muito o tempo de execução
# Com isso,é muito melhor utilizar uma série para fazer esse tipo de operação
nova_coluna = []
for i in df['qtdePontos']:
    nova_coluna.append(i + 100)
    
nova_coluna

# %%

# Criando uma nova coluna com o resultado da soma de 100 a cada elemento da coluna qtdePontos
df["pontos_100"] = df["qtdePontos"] + 100

# Para reatribuir valores a uma coluna é só usar o nome da coluna
# df["qtdePontos"] = df["qtdePontos"] + 100

# %%

df.head()

# %%

# Criando uma coluna para saber se a pessoa tem email ou twitch
# Operação linha a linha
# É possivel fazer com séries de mesmo tamanho
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%

# Criando uma coluna para saber se a pessoa tem email e twitch
# Operação linha a linha
df["flEmail"] * df["flTwitch"]

# %%
# Quantas redes sociais a pessoa tem cadastrada

df['qtdSocial'] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()
# %%

# Se a pessoa tem todas as redes sociais cadastradas
df['todas_social'] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head()
# %%

df["qtdePontos"].describe()
# %%

# Aplica o logaritmo natural a cada elemento da coluna qtdePontos utilizando a função numpy
# NumPy é utilizado para fazer operações matemáticas em arrays e matrizes de forma rápida e eficiente
np.log(df["qtdePontos"] + 1) # +1 para evitar log(0) que é indefinido
# %%
