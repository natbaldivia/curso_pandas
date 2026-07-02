# %%
idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,32
]
# calculando media
media = sum(idades) / len(idades)

print("Media: ",media)

#calculando variancia
diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

print("Variância: ",variancia)

# %%
import pandas as pd

series_idades = pd.Series(idades)
series_idades

# %%
# Estatísticas da série
media_idades = series_idades.mean()

var_idades = series_idades.var()

print("Média: ",media_idades)
print("Variância: ",var_idades)

summary = series_idades.describe()
print(summary)