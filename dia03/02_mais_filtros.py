# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv")
df.head()

# %%

# Filtra os produtos com idProduto 5 ou 11
filtro = (df['idProduto'] == 5) | (df['idProduto'] == 11)
df[filtro]
# %%

# Mesmo reultado do filtro acima
# isin() retorna uma serie booleana funcionando como filtro
filtro = df['idProduto'].isin([5, 11])
df[filtro]

# %%

clientes = pd.read_csv("../data/clientes.csv")
# Clientes com a data de criação registrada (não nula)
filtro = clientes['dtCriacao'].notnull()
# isna() retorna uma serie booleana com True para os valores nulos
# isnull() retorna uma serie booleana com True para os valores nulos    
# notna() retorna uma serie booleana com True para os valores não nulos
# notnull() retorna uma serie booleana com True para os valores não nulos

clientes[filtro]

# %%

# clientes['dtCriacao'].notna()
filtro = clientes['dtCriacao'].isna()
# Negação do filtro acima
~filtro

clientes[~filtro]

# %%
