# %%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  bbbb//bnnn# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes["qtdePontos"].sort_values()

# %%
# filtrando o cliente que tem a maior qtdePontos
max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %%
# os 5 primeiros clientes com maiores qtdePontos
clientes.sort_values(by="qtdePontos",ascending=False).head(5)["idCliente"]

# o sort_values retorna um dataframe novo com a ordem que eu pedi.
# não é uma view!

# %%
# dataframe de brinquedo ordenando pelo salário
# se o salário der empate, a idade deve ser critério de desempate
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533]
    }
)
brinquedo.sort_values(by=["salario", "idade"],ascending=[False, True])

