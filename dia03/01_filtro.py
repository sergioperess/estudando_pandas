#%%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv')
df.head()

# %%

# Funcionamento de um filtro na pratica
pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    filtro.append(i>=50)


resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])


resultado
filtro

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     }
)

# Retorna uma serie com o resultado booleano
# Resultado da operação logica feito com cada elemento da serie com um escalar (valor da comparação - 18)
filtro = brinquedo['idade'] >= 18

brinquedo

# %%

# O filtro e uma serie booleana e ele diz ao dataframe quais linhas devem ser retornadas (True) e quais devem ser descartadas (False)
# Retorna o dataframe filtrado com o resultado da comparação
brinquedo[filtro]

# %%

filtro = brinquedo['uf'] == 'sp'
filtro
brinquedo[filtro]

# %%

# Filtro para identificar as transações maiores ou iguais a 50 pontos
filtro = df['qtdePontos'] >= 50
df[filtro]

# %%

# Filtro para identificar as transações maiores ou iguais a 50 pontos e menores que 100
# O operador lógico AND (&) pode ser substituído por um asterisco (*)
filtro = (df["qtdePontos"] >=50) & (df["qtdePontos"] < 100)

#filtro = (df["qtdePontos"] >=50) * (df["qtdePontos"] < 100)

df[filtro]


# %%
# Filtro para identificar valores iguais a 1 ou 100
# Alt + 124 para o pipe (|) no teclado
# O pipe (|) representa o operador lógico OR e pode ser alterado por um mais (+)
filtro = (df["qtdePontos"] == 1) | (df["qtdePontos"]  == 100)
# filtro = (df["qtdePontos"] == 1) + (df["qtdePontos"]  == 100)

df[filtro]

# %%

# Filtro para identificar valores maiores que 0 e menores ou iguais a 50 e com data de criação maior ou igual a 2025-01-01
filtro = (df["qtdePontos"] > 0) & (df["qtdePontos"]  <= 50) & (df["dtCriacao"] >= '2025-01-01')
df[filtro]

# %%
