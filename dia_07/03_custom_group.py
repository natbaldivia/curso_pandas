# %%
import pandas as pd
import numpy as np 

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
# você pode criar funcões personalizadas pra fazer a agregação (group by)
def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) **2)

idades = pd.Series([45, 25, 25, 16, 35, 23, 29, 21])
diff_amp(idades)

# %%
(transacoes.groupby(by=["IdCliente"])
          .agg({
              "IdTransacao": ['count'],
              "QtdePontos": ['sum','mean',diff_amp]
          })
          
          
)
# %%
