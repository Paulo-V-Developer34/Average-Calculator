import pandas as pd
import matplotlib.pyplot as plt

# Dicionário de faturamento
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

df_faturamento = pd.DataFrame(dict_faturamento)

print("a média do faturamento é R${:.2f}.".format(df_faturamento['valor'].mean()))

#transformar o date
df_faturamento['data_ref'] = pd.to_datetime(df_faturamento['data_ref'])

#criando o gráfico de barras
df_faturamento.plot.bar(x='data_ref', y='valor')

#criando o gráfico de linhas
df_faturamento.plot.line(x='data_ref', y='valor')
