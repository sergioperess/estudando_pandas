# %% 

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%

clientes["dtCriacao"]
# %%

# Apaga todos os valores nulos da série
clientes.dropna()
# %%

# Apaga os valores quando a linha inteira for nula
clientes.dropna(how='all')

# %%

# Apaga os valores quando há ao menos um Na na linha
clientes.dropna(how='any')

# %%
df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

# %%

df.dropna()
# %%

df.dropna(how='all')
# %%

df.dropna(how='any')

# %%

# Utilizado para apagar os valores nulos de uma coluna específica
df.dropna(subset=["idade"])

# %%

# Nesse caso, o dropna irá apagar as linhas que possuem valores nulos em todas as colunas específicas
# Exemplo: Apagar as linhas que possuem valores nulos em idade e salario
df.dropna(how='all', subset=["idade", "salario"])

# %%

# Para apagar as linhas que possuem valores nulos em pelo menos uma coluna específica
# Exemplo: Apagar as linhas que possuem valores nulos em idade ou salario
df.dropna(how='any', subset=["idade", "salario"])

# %%

# Para substituir os valores nulos por um valor específico em uma coluna (Serie)
# Exemplo: Substituir os valores nulos em idade por 0
df["idade"] = df["idade"].fillna(0)

# %%

df = df.fillna({"idade": 0, "nome": "alguem"})
# %%

medias = df[["idade", "salario"]].mean()
df = df.fillna(medias)

# %%
# Evitar utilizar a média para preencher valores nulos, pois pode distorcer os dados
# Depende muito do contexto
# Uma forma de resolver isso é utilizar a média com base em dados completos
# Desse modo podemos utilizar um valor de média para difetentes grupos
df
# %%
