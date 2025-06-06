# %%
import pandas as pd
import sqlalchemy

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")


# %%

# Nome da tabela e a conexão com o banco
clientes = pd.read_sql_table(table_name="tb_customers", con=engine)
# %%

clientes.shape
# %%


# Não é uma boa ideia importar uma tabela inteira diretamente no python, pois pode ter muitos dados no banco
# Portanto é bom executar uma Query

query = "SELECT * FROM tb_customers LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100
# %%
