# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(indexs)

print(series_idades)
print(series_nomes)

# %%

df = pd.DataFrame() # um novo dataframe vazio

df["Idade"] = series_idades # Adiciona uma nova coluna chamada "Idade" com os dados da série de idades
df["Nome"] = series_nomes # Adiciona uma nova coluna chamada "Nome" com os dados da série de nomes

# DataFrame são estruturas de dados tabulares, semelhantes a uma planilha do Excel ou uma tabela SQL.
# Cada coluna pode ter um tipo de dado diferente (int, float, string, etc.)
# Uma DataFrame é uma coleção de Series, onde cada coluna é uma Series.
df = pd.DataFrame({
    "Idade": series_idades,
    "Nome": series_nomes,
})

# %%
# Exibe uma series
df["Nome"]

# %%
df["Idade"]
# %%

# Um DataFrame é uma coleção de Series, onde cada coluna é uma Series.
df

# %%

# Retorna uma série com os dados da primeira linha do DataFrame
df.iloc[0] # Acessa a primeira linha do DataFrame

# %%

# Ao pegar uma coluna, o pandas retorna uma Series onde os indices são os mesmos do DataFrame
print(df["Idade"])

# %%

# Ao pegar uma linha, o pandas retorna uma Series onde os indices são os nomes das colunas do DataFrame
# Para exibir uma linha, usamos o método iloc[] ou loc[]
print(df.iloc[0]) # Acessa a primeira linha do DataFrame

print(df.iloc[0]["Nome"]) # pega o nome da primeira linha
# %%

print(df.iloc[-1]) 

# Idade da ultima pessoa
print(df.iloc[-1]["Idade"]) # pega a idade da ultima linha

# %%

print(df.iloc[0]["Idade"]) # pega a idade da primeira linha