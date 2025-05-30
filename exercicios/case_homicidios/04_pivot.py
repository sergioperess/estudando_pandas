# %%

import pandas as pd

df = pd.read_csv("homicidios_consolidado.csv", sep=";")
df.head()
# %%

df_stack = df.set_index(["nome", "período"]).stack().reset_index()
# %%

df_stack.columns = ["nome", "período", "metrica", "valor"]
df_stack
# %%

# Mudar o DataFrame onde os preenche as celulas com o valores, os indices serão os index e as colunas passam a ser as columns
# Unstack é um caso particular do pivot_table
df_stack.pivot_table(values="valor", index=["nome", "período"], columns="metrica").reset_index()
# %%

# Pivotando a tabela e excluindo uma coluna
# Nesse caso ele faz a média das metricas a partir do valor em cada coluna 
df_stack.pivot_table(values="valor", index=["nome"], columns=["metrica"], aggfunc="mean")
# %%

# Contrario do pivot_table, volta na tabela stackada
df_stack.pivot_table(values="valor", index=["nome", "período"], columns="metrica").stack()
# %%
