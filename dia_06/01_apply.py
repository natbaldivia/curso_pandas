# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
# %%
idCliente = "fff940d1-0786-4ee5-a75a-3bbda4e50f7a"

def get_last_id(x):
    return x.split("-")[-1]

# %%
get_last_id("fff940d1-0786-4ee5-a75a-3bbda4e50f7a")

# %%
# criando uma lista para aplicar as alterações, e fazer o for com o append adicionando itens nessa lista
id_novo = []
for i in clientes["idCliente"]:
    id_novo.append(get_last_id(i))

clientes["novo_id"] = id_novo
clientes.head()

# %%
# no lugar de fazer o for, vamos usar o apply
# o apply aplica alterações linha a linha.
clientes["novo_id"] = clientes["idCliente"].apply(get_last_id)
clientes.head()

