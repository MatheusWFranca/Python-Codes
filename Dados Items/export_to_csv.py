import pandas as pd

df = pd.read_fwf('DadosDoItem\Item.txt', encoding='windows-1252', header=None)
df = df.iloc[10:]

df = df[0].str.split('|', expand=True)

df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

df = df[
    (df[3] == 'Manual') | 
    (df[3] == 'MRP') | 
    (df[3] == 'MPS') | 
    (df[3] == 'SIC')
    ]


df.columns= [
        "Item", 
        "Descricao", 
        "Tipo Man", 
        "Sist Ordem", 
        "Fornecedor",
        "Tipo Prod",
        "Chave Busca",
        "Revisão",
        "Cod Sinalizacao",
        "Grupo Item",
        "Comp",
        "Data Inicial",
        "Engenheiro",
        "Fam",
        "Descricao Fam",
        "Ult Tran Estoque",
        "Tipo Inventario"
        ]

df.to_csv("output.csv", encoding='windows-1252', index=False)
