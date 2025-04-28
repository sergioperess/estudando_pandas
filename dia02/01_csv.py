# %%

import pandas as pd

# Importando um arquivo CSV
# Retorna um DataFrame
df = pd.read_csv('../data/clientes.csv')
df

# %%

# Salvando um arquivo CSV
# Salva sem o indice
df.to_csv('clientes.csv')

# %%

# Salva o arquivo sem o indice
df.to_csv('clientes.csv', index=False)

# %%
# Salva em arquivo parquet(binário)
# O parquet é um formato de arquivo colunar, o que significa que os dados são armazenados em colunas em vez de linhas.
df.to_parquet("clientes.parquet", index=False)

# %%

df_2 = pd.read_parquet("clientes.parquet")
df_2

# %%

df.to_excel('clientes.xlsx', index=False)
# %%

df_3 = pd.read_excel('clientes.xlsx')
df_3
# %%
# Lendo um arquivo CSV com separador diferente
# O separador padrão é a vírgula, mas podemos usar outro separador, como o ponto e vírgula.
df_4 = pd.read_csv("../data/bobo.csv", sep=';')
df_4

# %%
