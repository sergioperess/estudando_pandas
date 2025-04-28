# %%

# Listas não possuem métodos para calcular média e variância, é uma função do phyton
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

media = sum(idades) / len(idades)
print("Media:",media)

# %%
diffs = 0
for idade in idades:
    diffs += (idade - media) ** 2
print("Soma dos quadrados:", diffs)

variancia = diffs / (len(idades) - 1)
print("Variancia:", variancia)

# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

# O ideal para series é usar elementos do mesmo tipo, mas não é obrigatório
series = pd.Series() # Cria uma série vazia, mesma coisa de criar uma lista vazia
series_idades = pd.Series(idades) # Cria uma série a partir de uma lista
print(series_idades)

# %%

# Estatísticas das séries
print("Média:", series_idades.mean()) # Calcula a média
print("Variancia:", series_idades.var()) # Calcula a variância
print("Desvio Padrão", series_idades.std()) # Calcula o desvio padrão
print("Máximo:", series_idades.max()) # Calcula o máximo
series_idades.describe() # Descreve a série, mostra contagem, média, desvio padrão, mínimo, máximo e quartis

# %%
