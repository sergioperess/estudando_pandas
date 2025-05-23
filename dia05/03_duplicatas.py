# %%

import pandas as pd

df = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva']
})

df
# %%

# Mantem a primeira ocorrência e remove as duplicatas
df.drop_duplicates()

# %%

# Mantem a última ocorrência e remove as duplicatas
df.drop_duplicates(keep='last')


# %%


df1 = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134],
})

df1
# %%

# Não dropamos as duplicatas, pois não há linhas inteiras(Series) duplicadas
df1.drop_duplicates(keep='last')

# %%

# Mantemos a primeira ocorrência e removemos as duplicatas onde o nome e sobrenome são iguais
df1.drop_duplicates(subset=['nome', 'sobrenome'])

# %%

# Mantemos a última ocorrência e removemos as duplicatas onde o nome e sobrenome são iguais
df1.drop_duplicates(subset=['nome', 'sobrenome'], keep='last')
# %%

df1 = df1.sort_values(by='salario', ascending=True)
# %%

df1.drop_duplicates(subset=['nome', 'sobrenome'], keep='last')
# %%

df1.drop_duplicates(subset=['nome', 'sobrenome'])
# %%

df1 = (df1.sort_values(by='salario', ascending=False)
        .drop_duplicates(subset=['nome', 'sobrenome']))

df1
# %%
