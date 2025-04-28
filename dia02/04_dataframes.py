# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")

df_clientes

# %%

# Mesma coisa que o limit no SQL
# df_clientes.head(10)  # Mostra as 10 primeiras linhas do DataFrame
df_clientes.head()  # Mostra as 5 primeiras linhas do DataFrame

# %%

df_clientes.tail()  # Mostra as 5 últimas linhas do DataFrame

# %%

df_clientes.sample(10)  # Mostra 10 linhas aleatórias do DataFrame

# %%

# Shape é um atributo do DataFrame que retorna uma tupla com a quantidade de linhas e colunas
# df_clientes.shape[0]  # Mostra a quantidade de linhas do DataFrame
df_clientes.shape  # Mostra a quantidade de linhas e colunas do DataFrame
# %%

print("Linhas:", df_clientes.shape[0])  # Mostra a quantidade de linhas do DataFrame
print("Colunas:", df_clientes.shape[1])  # Mostra a quantidade de colunas do DataFrame
# %%

# Nome das colunas do DataFrame
df_clientes.columns  # Mostra os nomes das colunas do DataFrame
# %%

df_clientes.index  # Mostra os índices do DataFrame
# %%

# Informações sobre o DataFrame
df_clientes.info()  # Mostra informações sobre o DataFrame
# %%

df_clientes.info(memory_usage="deep")  # Mostra informações sobre o DataFrame, incluindo o uso de memória
# %%

# retorna o tipo de dado de cada coluna do DataFrame em forma de série
df_clientes.dtypes  # Mostra os tipos de dados das colunas do DataFrame

# %%

df_clientes.dtypes["qtdePontos"]  
# %%

df_clientes.dtypes.iloc[2]  

# %%
