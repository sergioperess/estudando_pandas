# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()
# %%

# Agrupa por Cliente
transacoes.groupby(by=["idCliente"]).sum()
# %%

# Para computar uma estatistica de uma coluna 
transacoes.groupby(by=["idCliente"])["idTransacao"].count()
# %%

# Retorna um DataFrame com a contagem de transações por cliente onde o index é o idCliente
transacoes.groupby(by=["idCliente"])[["idTransacao"]].count()
# %%

# Quantidade de tranbsações por cliente
# Para que o index não seja o idCliente é necessário adicionar o método as_index no groupby
transacoes.groupby(by=["idCliente"], as_index=False)[["idTransacao"]].count()
# %%

# Quantidade de transações, média de pontos e total de pontos por clientes
# agg ou aggregate permite aplicar muitas funções ao mesmo tempo para fazer esse exercicio
# Necessário passar um dicionário onde a chave é o nome da coluna e o valor é uma lista com as funções que serão aplicadas
summary = (transacoes.groupby(by="idCliente", as_index=False)
            .agg({"idTransacao": ["count"],
                "qtdePontos": ["sum", "mean"]})
            )
# %%

summary.columns
# %%

# Maneira de acessar uma série em um DataFrame com múltiplos índices
summary["qtdePontos"]["mean"]
summary[("qtdePontos","mean")]
# %%

# Definindo as colunas do DataFrame para acabar com o MultiIndex
summary.columns = ["idCliente", "qtdeTransacao", 'totalPontos', 'avgPontos']
summary
# %%
