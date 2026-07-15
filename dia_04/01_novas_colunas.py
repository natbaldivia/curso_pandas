# %%
import pandas as pd
import numpy as np
df = pd.read_csv("../data/clientes.csv",sep=";")
df.head()

# %%
# adicionando uma coluna 'pontos_100', onne eu somo 'qtdePontos' + 100
df["pontos_100"] = df["qtdePontos"] + 100

# %%
# usuario tem twitch ou email
df["Twitch_ou_email"] = df["flTwitch"] + df["flEmail"]
df.head()

# %%
# usuario tem twitch E email
df["flEmail"] * df["flTwitch"]

# %%
# quantas redes sociais o usuario tem cadastrado
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()

# %%
df["qtdePontos"].describe()

# %%
df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()

# %%
import matplotlib.pyplot as plt

plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()