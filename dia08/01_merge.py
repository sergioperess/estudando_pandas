# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%

# Combine com a tabela clientes com LEFTJOIN onde a chave é idCleinte
# Junta a tabela de clientes com a tabela de transações
transacoes.merge(right=clientes, how="left", on="idCliente").head()
# %%

# Sufixes adiciona nomes de colunas para evitar conflitos
transacoes.merge(right=clientes, 
                how="left", 
                on="idCliente",
                suffixes=["Transação", "Cliente"],
                ).head()
# %%

df_1 = pd.DataFrame({
    "transacao": [1,2,3,4,5],
    "nome": ["t1", "t2", "t3", "t4", "t5"],
    "idCliente": [1,2,3,2,2],
    "valor": [10,45,32,17,87],
})

df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "nome": ["teo", "nah", "mah", "jose"],
})
# %%

# utilizado para especificar as colunas de junção
df_1.merge(right=df_2, left_on=["idCliente"], right_on=["id"],
           how="left", suffixes=["Transacao", "Cliente"])

# %%


