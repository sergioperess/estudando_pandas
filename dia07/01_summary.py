# %%

import pandas as pd

idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]
idades = pd.Series(idades)
idades

# %%

idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()

# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%

# Aplica a agregação em uma coluna do DataFrame (Série)
clientes["flTwitch"].sum()
clientes["flTwitch"].mean()
# %%

# Aplica a agregação em cada uma das colunas do DataFrame
redes_sociais = ["flEmail",	"flTwitch",	"flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].sum()
clientes[redes_sociais].mean()

# %%

# Pega somente as colunas que são do tipo númerico
filtro = clientes.dtypes == "object"
num_columns = clientes.dtypes[~filtro].index.tolist()

clientes[num_columns].mean()

# %%

# Descreve cada uma das colunas
clientes[num_columns].describe()

# %%
