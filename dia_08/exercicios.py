# %%
# quem teve mais transações de Streak?

import pandas as pd

# %%
transacoes = pd.read_csv("../data/transacoes.csv",sep=";")

transacao_produto = pd.read_csv("../data/transacao_produto.csv",sep=";")

produtos = pd.read_csv("../data/produtos.csv",sep=";")

# %%
cliente_transacao_produto = transacoes.merge(transacao_produto,
                 on="IdTransacao",
                 how='left')

cliente_transacao_produto[["IdTransacao","IdCliente","IdProduto"]]

# %%
df_full = cliente_transacao_produto.merge(produtos,on="IdProduto",how="left")

# %%
filtro = df_full["DescNomeProduto"] == "Presença Streak"
(df_full[filtro].groupby(by=["IdCliente"])["IdTransacao"]
                .count()
                .sort_values(ascending=False)
)

# %%
# VERSÃO MAIS PERFORMÁTICA E AVANÇADA:

#aplicar filtro nos produtos
produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

(transacoes.merge(transacao_produto,on="IdTransacao",how='left')
           .merge(produtos, on="IdProduto", how="right")
           .groupby(by="IdCliente")["IdTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1)
)