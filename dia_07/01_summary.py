# %%
import pandas as pd

idades = [23, 34, 25, 85, 65, 24, 75, 34, 54, 25, 16, 10, 24]

idades = pd.Series(idades)

# %%
idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes["flTwitch"].sum()
clientes["flTwitch"].mean()

redes_sociais = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
clientes[redes_sociais].sum()

# %%
# filtrando colunas que são "object" (string)
filtro = clientes.dtypes == "object"

# filtrando colunas que não são "object" (o ~ nega o argumento)
num_columns = clientes.dtypes[~filtro].index.tolist()

# a média de todas as colunas numéricas do dataframe
clientes[num_columns].mean()

#aplicando o describe para ter as estatisticas do dataframe
clientes[num_columns].describe()