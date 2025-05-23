# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%

# Os tipos dos elementos da série são int
df["qtdePontos"]

# %%

# Converte os elementos da série para float
df["qtdePontos"].astype(float)

# %%

# Converte os elementos da série para string
# astype retorna uma série com os elementos convertidos
df["qtdePontos"].astype(str)

# %%

# Converte os elementos da série para string
df["qtdePontos"].astype(str).astype(int)

# %%

# Da erro, pois há uma data inválida na série (0000-00-00 00:00:00.000)
# para isso devemos fazer um replace para adicionar uma data válida e assim converter
pd.to_datetime(df["dtCriacao"])
# %%

# Substitui elementos de uma série por outros elementos
# df["dtCriacao"].replace({"2020-01-01": "2020-01-02"})
# Necessário utilizar um dictionário para substituir os elementos
df["dtCriacao"].replace({"0000-00-00 00:00:00.000":"2024-02-01 09:00:00.000"}, inplace=True)

# Não altera a série original, apenas retorna uma nova série
# Para isso é necessário utilizar o parâmetro inplace=True ou reatribuir o resultado a df["dtCriacao"]

# %%

df["dtCriacao"]

# %%

pd.to_datetime(df["dtCriacao"])
# %%

# Geralmente encontrado dessa forma
# Valores que desejo substituir
replace = {"0000-00-00 00:00:00.000":"2024-02-01 09:00:00.000"}

# Aplicando a conversão na série apos o replace aplicado e reatribuindo o resultado a série original
df["dtCriacao"] = pd.to_datetime(df["dtCriacao"].replace(replace))

# %%

# Após converter para datetime, podemos utilizar os métodos de datetime
# Exemplo: extrair o ano da data utilizando dt.year
df["dtCriacao"].dt.year

# %%

df["dtCriacao"].dt.month_name()
# %%
