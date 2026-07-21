# %%
import pandas as pd
import os

def read_file(file_name:str):
    df = (pd.read_csv(f"../data/ipea/{file_name}.csv", sep=";") # ler o arquivo
            .rename(columns={"valor":file_name}) # renomear coluna
            .set_index(["nome", "período"]) # definir índices
            .drop(["cod"],axis=1)) #removendo coluna que não será usada
    return df

# %%
# acessando todos os arquivos do diretorio ipea
file_names = os.listdir("../data/ipea")

# lendo todos os arquivos e colocando numa lista de dataframes
dfs = []
for i in file_names:
    file_name = i.split(".")[0]
    dfs.append( read_file(file_name) )

# %%
# teste acessando só homicidios-mulheres
dfs[-5]

# %%
# concatenando unindo todos os dataframes em um só:
df_full = (pd.concat(dfs,axis=1)
             .reset_index()
             .sort_values(["período","nome"]))

df_full.to_csv("homicidios_consolidado.csv", index=False, sep=";")


