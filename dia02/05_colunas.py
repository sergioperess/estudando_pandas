# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df
# %%

df.shape  # Quantidade de linhas e colunas do DataFrame

# %%

df.info(memory_usage="deep")  # Informações sobre o DataFrame, incluindo tipos de dados e uso de memória

# %%
df.dtypes  # Tipos de dados das colunas do DataFrame

# %%

# Chave do dicionário: nome da coluna
# Valor do dicionário: novo nome da coluna
df = df.rename(columns={
                        "qtdePontos": "qtPontos", 
                        "descSistemaOrigem": "SistemaOrigem"
                        })  # Renomeia a coluna "qtdePontos" para "qtPontos"

# Não altera o DataFrame original, apenas retorna uma cópia do DataFrame com a coluna renomeada
# por isso, precisamos atribuir o resultado a uma variável ou usar o parâmetro inplace=True
# %%

df.dtypes  # Tipos de dados das colunas do DataFrame após renomear a coluna
# %%

df["idCliente"]  # Seleciona a coluna "idCliente" do DataFrame
# %%

# Rettorna um dataframe com as colunas "idCliente" e "qtPontos"
df[["idCliente", "qtPontos"]]  # Seleciona as colunas "idCliente" e "qtPontos" do DataFrame
# %%

# Retorna um dataframe com uma única coluna "idCliente"
df[["idCliente"]]

# Desse modo, ao passar uma lista de chaves, o pandas retorna um DataFrame com as colunas selecionadas
# independente de quantos elementos a lista tenha
# Importante: Para trabalhar com DataFrames mesmo com uma única coluna

# %%

# SELECT * FROM df
df
# %%
# SELECT idCliente FROM df

df[["idCliente"]]  # Seleciona a coluna "idCliente" do DataFrame
# %%

#SELECT idCliente, qtPontos FROM df LIMIT 5

df[["idCliente", "qtPontos"]].head() # Seleciona as 5 primeiras linhas do DataFrame
# %%

# SELECT idCliente, idTransacao, qtPontos FROM df LIMIT 5 
df[["idCliente", "idTransacao","qtPontos"]].sample(5)

# Para reorderar as colunas, basta passar a lista de colunas na ordem desejada


# %%

# Ordena as colunas do DataFrame em ordem alfabética
colunas = df.columns.to_list()  # Pega os nomes das colunas do DataFrame e transforma em uma lista  
colunas.sort()  
colunas  

df = df[colunas]  # Seleciona as colunas do DataFrame na ordem alfabética

df
# %%
