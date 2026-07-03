# %%
import pandas as pd

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39
]

series_idades = pd.Series(idades)
series_idades
series_idades[0]
series_idades[-1] # aqui ele apresenta um KeyError, pois não existe Key (chave) que seja -1 
# o indice fica vinculado ao valor
# %%
series_idades = series_idades.sort_values()
series_idades
# %%
#como fazer pra pegar o primeiro ou ultimo valor sem precisar saber sua posição?
series_idades.iloc[0] # ao usar o iloc usamos sua posição, e não a chave associada do indice
series_idades.iloc[-1]

# com o iloc é possivel fazer slice (pegar mais de um elemento em uma série)
series_idades.iloc[:3]

# %%
# pra pegar do último para o primeiro, da pra fazer igual listas dessa maneira:
series_idades.iloc[::-1]

# %%
# é possivel setar os índices também

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39
]

indexs = [
    "Teo","Maria","Jose","Luis","Ana",
    "Nah","Dani","Mah","Fer","Nanda",
    "naty","Nih","Pedro","Kozato","Tito"
]
series_idades = pd.Series(idades,index=indexs)
series_idades

# %%
series_idades["Pedro"]
series_idades.loc["Pedro"]

#iloc => navega nas linhas
#loc => navega nos indices

