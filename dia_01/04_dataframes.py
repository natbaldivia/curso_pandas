# %%

import pandas as pd

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39
]

nomes = [
    "Teo","Maria","Jose","Luis","Ana",
    "Nah","Dani","Mah","Fer","Nanda",
    "naty","Nih","Pedro","Kozato","Kozato"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

df.iloc[0] # dessa forma ele considera as colunas como índices.
# e está retornando uma série onde cada elemento da série é uma coluna do dataframe.





