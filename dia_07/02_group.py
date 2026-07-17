# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
#transacoes.head()
transacoes.groupby(by=["IdCliente"]).count() 

# %%
# qtde de transacoes por cliente
transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count()

# %%
# total de pontos por cliente
transacoes.groupby(by=["IdCliente"])[["QtdePontos"]].sum()

# %%
# média de pontos por transação
transacoes.groupby(by=["IdCliente"], as_index=False)[["QtdePontos"]].mean()

# %%
# qtde transacçoes
# total pontos
# pontos/ transacoes

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
          .agg({"IdTransacao": ['count'],
                "QtdePontos": ['sum', 'mean']})
                )

summary.columns
# como faço para acessar uma coluna num multiindex
summary["QtdePontos"]['mean']

# ou
summary[("QtdePontos", "mean")]
# ou (versão mais acessivel), renomear as colunas

summary.columns = ["IdCliente", "QtdeTransacao", "TotalPontos", "AvgPontos"]

summary