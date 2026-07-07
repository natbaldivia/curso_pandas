# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv",sep=";")

df.shape

df.info(memory_usage='deep')

# %%
df.dtypes

# %%
# COMO RENOMEAR COLUNAS

renamed_columns = {
        "QtdePontos": "qtPontos",
        "DescSistemaOrigem": "SistemaOrigem"
}

df = df.rename(columns=renamed_columns)
df
# df.rename(columns=renamed_columns, inplace=True) # com o inplace vc altera o proprio dataframe sem precisar reatribuir


# %%
df["IdCliente"] #retorna uma série

# %%
df[["IdCliente","qtPontos"]] #retorna um dataframe

# %%
# COMPARAÇÃO COM SQL
# SELECT * FROM df
df

# SELECT IdCliente FROM df
df[["IdCliente"]]

# SELECT IdCliente, qtPontos FROM df LIMIT 5
df[["IdCliente","qtPontos"]].head(5)

# SELECT IdCliente, IdTransacao, qtPontos FROM df LIMIT 5
df[["IdCliente","IdTransacao","qtPontos"]].head(5)

# %%
colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]
df