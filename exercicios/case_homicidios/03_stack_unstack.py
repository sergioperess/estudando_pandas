# %%
import pandas as pd

df = pd.read_csv("homicidios_consolidado.csv", sep=";")

df.head()
# %%

# Pegar colunas e transformar em linhas, empilhando elas, repetindo as métricas
df = df.set_index(["nome", "período"])
df_stack = df.stack()
# %%

# E uma série
df_stack.head()
# %%

# Para transformar em DataFrame é necessário resetar o index
df_stack = df_stack.reset_index()
df_stack.columns = ["nome", "período", "metrica", "valor"]
df_stack
# %%

# A volta para o formato original é feita com unstack]
# Para fazer isso e necessário fazer o set_index novamente
df_stack = df_stack.set_index(["nome", "período", "metrica"])
df_unstack = df_stack.unstack().reset_index()

# %%
metricas = df_unstack.columns.droplevel(0)[2:].tolist()

df_unstack.columns = ["nome", "período"] + metricas
# %%

df_unstack
# %%
