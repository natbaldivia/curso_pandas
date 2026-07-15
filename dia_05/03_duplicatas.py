# %%
import pandas as pd

df = pd.DataFrame(
    {
        "nome": ["teo", "lara", "nah", "bia", "mah","lara", "mah", "mah"],
        "sobrenome": ["calvo", "calvo", "ataide", "ataide", "silva", "silva", "silva", "silva"],
        "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
    }
)
df

# %%
# o drop_duplicates mantém somente a primeira
df.drop_duplicates()

# %%
# se a gente informar o 'keep', ele vai manter conforme nossa escolha
df.drop_duplicates(keep='last')

# %%
# ordenar a coluna 'salario' antes de remover a duplicata
df = df.sort_values("salario", ascending=False)
# podemos escolher a coluna que sera considerada pra remover as duplicatas (subset)
df.drop_duplicates(keep="last", subset=["nome", "sobrenome"]) 