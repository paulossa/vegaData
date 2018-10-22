import pandas as pd


cols = ['situacao', 'votos', 'ano', 'turno']

data = pd.read_csv('comp.csv')[cols]
data = data.query('situacao in ["COMPARECIMENTO", "ABSTENÇÃO"]')

print("Data antes de processo ")
#print(data)

sumarioGeral = data.groupby(['situacao', 'ano', 'turno']).sum()

s1 = data.query('ano == 1989').sum()        
print(s1)


for it in sumarioGeral.items():
    print(it[0])
   #print(it[1])
sumarioGeral.to_csv('myCsv.csv', header=True)