# %%

# 06.04 - Quem teve masi transação de streak

import pandas as pd

# %%
transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()
# %%

transacao_poduto = pd.read_csv("../data/transacao_produto.csv")
transacao_poduto.head()
# %%

produtos = pd.read_csv("../data/produtos.csv")
produtos.head()
# %%

cliente_transacao_produto = transacoes.merge(
    right=transacao_poduto, 
    how="left", 
    on="idTransacao",
)

cliente_transacao_produto[["idCliente", "idProduto", "idTransacao"]]

# %%

df_full = cliente_transacao_produto.merge(right=produtos, how = "left", on=["idProduto"])
# %%

df_full = df_full[df_full["descProduto"] == "Presença Streak"]
df_full

# %%

df_full.groupby(by=["idCliente"])["idTransacao"].count().sort_values(ascending=False)
# %%


produtos = produtos[produtos["descProduto"] == "Presença Streak"] 

(transacoes.merge(
    right=transacao_poduto, 
    how="left", 
    on="idTransacao",
).merge(produtos, how="right", on=["idProduto"])
 .groupby(by=["idCliente"])["idTransacao"].count()
 .sort_values(ascending=False)
)
# %%
