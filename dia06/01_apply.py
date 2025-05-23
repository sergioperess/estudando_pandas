# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()
# %%

# Separar a String em duas, pegar a ultima parcela depois do (-)
def get_last_id(x):
    return x.split("-")[-1]

novo_id = []

for i in df["idCliente"]:
    novo_id.append(get_last_id(i))
    
df["Novo_ID"] = novo_id
df.head()
# %%

# Separar a String em duas, pegar a ultima parcela depois do (-) com apply
# Método utilizado para aplicar uma função (métodos) em todos os elementos do DF 
df["idCliente"].apply(get_last_id)

# %%
