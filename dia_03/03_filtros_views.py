# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes.head()

filtro = clientes["qtdePontos"] == 0
clientes[filtro]

# %%
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1

# %%
clientes_0
#quando fazemos um filtro no dataframe, ele não retorna uma cópia
#ele cria uma VIEW. Esse clientes_0 está apontando para as mesmas linhas de clientes, mas só quando o filtro é True
# ao criar uma cópia usando o .copy() , isso pode custar memória, pois vc estará duplicando dados.
