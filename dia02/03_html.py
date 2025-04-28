# %%

import pandas as pd

# Pega todas as tabelas encontradas em uma página e retorna uma lista de DataFrames
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs
# %%

len(dfs)  # Quantidade de tabelas encontradas na página
dfs[0]  # Primeira tabela encontrada na página
# %%

# A tabela que queremos
df_uf = dfs[1]  # Seleciona a tabela de Unidades Federativas
df_uf.to_csv("ufs.csv", sep=';', index=False)  # Salva a tabela em um arquivo CSV
# %%
