# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()
# %%

# 05.05 - Selecione a primeira transação diária de cada cliente.

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date


transacoes = transacoes.sort_values("dtCriacao", ascending=True)
transacoes.drop_duplicates(keep="first",subset=["idCliente", "dia"])

# %%

# Quanto tempo o cliente ficou logado no dia (Sessão diária)

# Criação da primeira(first) e ultima(last) aparição da pessoa no dia
first = transacoes.drop_duplicates(keep="first",subset=["idCliente", "dia"])
last = transacoes.drop_duplicates(keep="last",subset=["idCliente", "dia"])

# %%

last