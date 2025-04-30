# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%

# Ordenando a coluna qtdePontos
# Ordena uma série e retorna uma nova série
clientes["qtdePontos"].sort_values()

# %%

clientes
# %%

# Descobre a linha que tem o maior número de pontos	
max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %%
# Ordena o DataFrame do maior para o menor
# Retorna um DataFrame novo com os dados ordenados e não uma view do original
clientes.sort_values(by="qtdePontos", ascending=False).head()

# %%

# Exibe os Ids dos 5 clientes com mais pontos em uma série
(clientes.sort_values(by="qtdePontos", ascending=False)
        .head(5)["idCliente"])
        
# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    }
)

brinquedo
# %%

# Ordena o DataFrame primeiro pelo salario e depois pela idade
brinquedo.sort_values(by=["salario", "idade"], ascending=False)

# %%

# Ordena o DataFrame primeiro pelo salario e depois pela idade, onde a idade é crescente
# e o salario é decrescente
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
# %%
