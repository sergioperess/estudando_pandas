# %%

import pandas as pd

df_geral = pd.read_csv("../data/ipea/homicidios.csv", sep=";")

df_geral = df_geral.rename(columns={"valor": "homicidios"})

df_geral.head()
# %%

df_negros = pd.read_csv("../data/ipea/homicidios-negros.csv", sep=";")
df_negros = df_negros.rename(columns={"valor": "homicidios-negros"})
df_negros.head()
# %%

df_geral = df_geral.set_index(["nome", "período"])
df_negros = df_negros.set_index(["nome", "período"])

# %%

pd.concat([df_geral,df_negros], axis=1)
# %%


# %%



