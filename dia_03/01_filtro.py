# %%
import pandas as pd
# 2 condições lógicas de filtro: & (and)
df = pd.read_csv("../data/transacoes.csv",sep=";")
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100) 
df[filtro] 

# %%
# 2 condições lógicas de filtro: | (or)
df = pd.read_csv("../data/transacoes.csv",sep=";")
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] > 1000) 
df[filtro] 
# %%
pontos = [10,1,1,1,50,100,130,1,1,30,25,50]

valores_50_mais = []

for i in pontos:
    if i >=50:
        valores_50_mais.append(i)

valores_50_mais

# %%
brinquedo = pd.DataFrame(
    {
        "nome":["Shadow","Natalia","Carla","João"],
        "idade":[4, 34, 35, 23],
        "UF":["SP", "MG", "SC", "PR"]
    }
)
filtro = brinquedo["idade"] >= 18

brinquedo[filtro]