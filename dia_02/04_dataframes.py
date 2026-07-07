# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv",sep=";")
df_clientes

# %%
# AMOSTRAS
df_clientes.head(n=10) # cabeçalho

# %%
df_clientes.tail(10) # ultimas linhas

# %%
df_clientes.sample(10) # uma amostra aleatoria

# %%
df_clientes.shape # o shape é um atributo,não um método
#ele retorna uma tupla (numero de linhas,numero de colunas)
df_clientes.columns

df_clientes.index

# %%
df_clientes.info(memory_usage='deep')

# %%
df_clientes.dtypes["DtAtualizacao"]
df_clientes.dtypes["qtdePontos"]
# dtypes é uma serie que mostra os valores da tipagem de cada coluna

