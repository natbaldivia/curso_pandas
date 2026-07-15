# %%
import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")

df["qtdePontos"].astype(float)

# %%

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])
df["DtCriacao"].dt.month_name()
# %%
df["DtCriacao"].replace({"2024-02-01 00:00:00.000": "2024-02-01 09:00:00.000"})

# %%
df["DtCriacao"]
# %%
