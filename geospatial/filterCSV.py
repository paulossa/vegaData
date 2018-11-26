import pandas as pd 

data = pd.read_csv("Basico_RJ.csv", sep=";", encoding="latin_1")
print(data.shape)

data2 = data.query("Nome_do_municipio == 'RIO DE JANEIRO'")
print(data2.describe())
data2 = data2.drop(columns=['Unnamed: 33'])
print(data2.describe())
data2.to_csv('filtered.csv', encoding='utf-8', index=False, index_label=False)