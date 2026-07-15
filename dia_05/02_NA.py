# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
# removendo/ignorando todos as linhas que contem ao menos 1 NA e colocando numa view

clientes.dropna()
# ou
clientes.dropna(how="any")

# para considerar q a linha inteira seja de NA:
clientes.dropna(how="all")
# %%

# dataframe de brinquedo
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", None, "nah", "jose"],
        "idade": [None, None, 35, 42],
        "salario": [2345, 4533, None, 4533]
    }
)
#dropando o NA de um dataframe onde a idade for NA
brinquedo.dropna(how="all",subset=["idade"])

# %%
# como preencher os dados faltantes numa coluna especifica

brinquedo["idade"].fillna(0)

# preencher os dados faltantes no dataset inteiro
brinquedo.fillna(0)

# %%
brinquedo.fillna({"nome": "alguém","idade": 0})

# %%
medias = brinquedo[["idade", "salario"]].mean()
brinquedo.fillna(medias)