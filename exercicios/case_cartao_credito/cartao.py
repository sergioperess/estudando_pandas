# %%
# Exercicio é calcular o valor a ser pago em cada mes, considerando o valor da venda, a quantidade de parcelas e a data da transação.

import pandas as pd

df = pd.read_csv('dados_cartao.csv', sep=";")
df
# %%

df["dtTransacao"] =  pd.to_datetime(df["dtTransacao"])
df
# %%

df["valorParcela"] = df["vlVenda"] / df["qtParcelas"]
# df["vlParcelaUnica"] = df.apply(lambda row: [row["valorParcela"]] * row["qtParcelas"], axis=1)
df["ordemParcela"] = df.apply(lambda row: [i for i in range (row["qtParcelas"])], axis=1)
df
# %%

# Pega a lista de parcelas da série e cria em linhas
df_explode = df.explode("ordemParcela")
df_explode
# %%

df_explode["dtParcela"] = df_explode.apply(lambda row: row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"]), axis=1)

df_explode
# %%

