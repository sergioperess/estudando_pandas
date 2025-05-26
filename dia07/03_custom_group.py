# %%

import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes. head()
# %%

# Método para calcular a distância da amplitude da média para testar o groupby com funções customizadas

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude-media)**2)

def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days
# %%

# É possível criar funções personalizadas para aplicar no groupby
summary = (transacoes.groupby(by=["idCliente"])
            .agg(
                {
                    "idTransacao": ["count"],
                    "qtdePontos": ["sum", "mean", diff_amp],
                    "dtCriacao": life_time
                }
            )
            )
# %%

summary.columns = ["qtdeTransacoes", "totalPontos", "avgPontos", "diffAmp", "lifeTime"]
summary
# %%
