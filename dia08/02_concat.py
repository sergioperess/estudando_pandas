# %% 

import pandas as pd
# %%

df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})

df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["kozato", "laura", "dan",],
    "idade":[32,29,31],
})

df_03 = pd.DataFrame({
    "idade": [32,34,19,54,33]
})
# %%

# Concat é utilizado para empilhar valores
# Lista de DataFrames para concatenar
dfs = [df, df_02]
pd.concat(dfs, ignore_index=True)
# %%

# Concatenou os DataFrames da esquerda para a direita 
pd.concat([df, df_03], axis=1)

# %%

# Ele utiliza o indice para a concatenação, portanto não funciona ordenar as colunas
df_03 = df_03.sort_values(by="idade")
pd.concat([df, df_03], axis=1)

# %%

# Para ordenar as colunas e concatenar, é necessario resetar o índice
df_03 = df_03.sort_values(by="idade").reset_index(drop=True)
pd.concat([df, df_03], axis=1)
# %%
