# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

series = pd.Series() 
series_idades = pd.Series(idades)
print(series_idades)

# %%

print("Primeiro:", idades[0])
print("Último:", idades[-1])

# %%

# Os indices nas series funcionam da mesma forma que as chaves de um dicionário
print("Primeira idade na série:", series_idades[0])
# print("Última idade na série:", series_idades[-1]) # Erro, não existe o índice -1

print("Última idade na série:", series_idades[len(series_idades) - 1])

# %%

# O indice permanece vinculado ao elemento da serie mesmo que a série seja alterada
series_idades = series_idades.sort_values()
print(series_idades)

print("Primeira idade na série:", series_idades[0])
# %%

# Método utilizado para acessar o primeiro elemento da série por posição e não por indice
print("Primeira idade na série ordenada:", series_idades.iloc[0])
print("Última idade na série ordenada:", series_idades.iloc[-1])

# Olha para a série como se fosse uma 'lista' e portanto aceita o -1
# Porque olha para a serie por posição e não por indice

# %%

series_idades.iloc[:3]
# %%

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

# Criando uma série com os indices personalizados
series_idades = pd.Series(idades, index=indexs)
print(series_idades)

# %%

# Indexes associados ao valor
print("Idade de Pedro:", series_idades["Pedro"]) 
print("Primeira idade na série com indexes personalizados:", series_idades.iloc[0])
print("Última idade na série com indexes personalizados:", series_idades.iloc[-1])

# iloc navega nas linhas da serie independente do index
# loc navega pelos indices, mas em uma serie já se navega por indices, portanto pode ocultar o loc
# loc é mais utilizado em dataframes, onde o index pode ser diferente do valor

print("Idade de Téo:", series_idades.loc["Téo"]) # Navegando pelo index
print("Idade de Téo:", series_idades["Téo"]) # A mesma coisa que o loc, mas mais simples de ler



# %%
