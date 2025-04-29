# %%

import pandas as pd

# O filtro não cria uma cópia do dataframe, mas sim uma view (visão) do dataframe original
# O filtro aponta para as linhas em que a condição é verdadeira, mas não altera o dataframe original 
# O dataframe original não é alterado, mas sim a view (visão) do dataframe original
clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy()  # Cria uma cópia do dataframe filtrado
# Duplicando dados e pode custar memória, mas ests desassociando os dataframes

clientes_0
# %%

clientes_0['flag_1'] = 1   

# %%

clientes_0

# %%
clientes
# %%

# Desassociando variáveis, isso serve para datraframes tambem
A = [1,2]
B = A.copy()
print("A:", A)
print("B:", B)

B.append("fodase")
print("A:", A)
print("B:", B)
# %%
