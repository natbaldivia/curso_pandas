# %%
import pandas as pd

df = pd.read_csv("../data/ufs.csv", sep=";")
df
# %%
df.dtypes

# %%

def str_to_float(x:str):
    x = float(x.replace(" ","")
               .replace(",","."))
    return x
# %%
df["Área (km²)"] = df["Área (km²)"].apply(str_to_float)
# %%
df.dtypes

# %%
df["População (Censo 2022)"] = df["População (Censo 2022)"].apply(str_to_float)
df

# %%
df["PIB (2015)"] = df["PIB (2015)"].apply(str_to_float)
df["PIB per capita (R$) (2015)"] = df["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%
x = "73,9 anos"
def exp_to_anos(exp):
    return float(exp.replace(" ", "")
                  .replace("anos", "")
                  .replace(",", "."))

df["Expectativa de vida (2016)"] = df["Expectativa de vida (2016)"].apply(exp_to_anos)

df.dtypes
# %%
# como faz para fazer um CASE WHEN

def uf_to_regiao(df):
    if df in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif df in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif df in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    elif df in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif df in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
df["Região"] = df["Unidade federativa"].apply(uf_to_regiao)



# %%
def mortalidade_to_float(x):
    x = float(x.replace("‰", "")
               .replace(",", "."))
    return x

df["Mortalidade infantil (/1000)"] = df["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%
df["IDH (2010)"] = df["IDH (2010)"].apply(str_to_float)
# %%
# até agora estamos fazendo o apply na série (uma única coluna). 
# agora vamos fazer o apply no dataframe

# se o PIB per capita for > 30000
# e a mortalidade < 15 / 1000
# e IDH > 700
# -> "parece bom"
# else, "não parece bom"

linha = df.iloc[0]

(linha["PIB per capita (R$) (2015)"] > 30000 
and linha["Mortalidade infantil (/1000)"] < 15 
and linha["IDH (2010)"] > 0.700)

# %%
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and 
            linha["Mortalidade infantil (/1000)"] < 15 and
            linha["IDH (2010)"] > 0.700)

# %%
# axis=0 == colunas ; axis=1 == linhas
df["parece_bom"] = df.apply(classifica_bom, axis=1)

# %%
df.dtypes
# %%

filtro = df["parece_bom"] == True
df[filtro]