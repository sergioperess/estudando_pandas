# %%

import pandas as pd

# Recupera os dados que estão na área de transferência (clipboard) e os armazena em um DataFrame
# Comando para copiar os dados: Ctrl + C (Windows) ou Cmd + C (Mac)
df = pd.read_clipboard(sep=";")
df

