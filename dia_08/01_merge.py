# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes["idCliente"] = transacoes["IdCliente"]
transacoes.head()
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# trazer as informações do cliente a partir do id da transação

# %%
transacoes.merge(right=clientes, 
                 how='left', 
                 on=["idCliente"], 
                 suffixes=["Transacoes", "Clientes"] # renomeia as tabelas cujas colunas são repetidas
                 )

#inner = interseção
#right = tabela fixa é a da direita
#left = tabela fixa é a da esquerda

# %%
df_1 = pd.DataFrame({
    "transacao": [1,2,3,4,5],
    "nome":["t1","t2","t3","t4","t5"],
    "idCliente": [1,2,3,2,2],
    "valor": [10,45,32,17,87],
})
df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "nome": ["teo","nah","mah","jose"],
})
df_1.merge(df_2, 
           left_on = ["idCliente"], 
           right_on = ["id"], 
           how='left',
           suffixes=["Transacao","Cliente"])