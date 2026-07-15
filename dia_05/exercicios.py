# %%
import pandas as pd
import numpy as np

# %%
# 01 - crie uma coluna nova "twitch_pontos" que é 
# resultado da multiplicação do saldo de pontos e a marcação da twitch

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes["twitch_pontos"] = clientes["qtdePontos"] * clientes["flTwitch"]
clientes.head()

# %%
# 02 - Aplique o log na coluna de saldo de pontos, criando uma nova coluna

clientes["logPontos"] = np.log(clientes["qtdePontos"])
clientes.head()

# %%
# 03 - Crie uma coluna que sinalize se a pessoa tem vinculo com qualquer uma rede social

clientes["ao_menos_uma_social"] = clientes["flTwitch"] + clientes["flYouTube"] + clientes["flBlueSky"] + clientes["flInstagram"]
clientes.head()

# %%
# 04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor? 

clientes.sort_values(by="qtdePontos", ascending=False).head(1)["idCliente"]

clientes.sort_values(by="qtdePontos", ascending=True).head(1)["idCliente"]

# %%
# 05 - Selecione a primeira transação diária de cada cliente
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
transacoes = transacoes.sort_values("DtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes.drop_duplicates(keep="first",subset=["IdCliente", "data"])

# %%
transacoes = transacoes.sort_values("DtCriacao")
first = transacoes.drop_duplicates(keep="first",subset=["IdCliente", "data"])

last = transacoes.drop_duplicates(keep="last",subset=["IdCliente", "data"])

pd.concat([last, first])