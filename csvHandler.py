import pandas as pd


cols = ['situacao', 'votos', 'ano', 'turno']

data = pd.read_csv('comp.csv')[cols]
data = data.query('situacao in ["COMPARECIMENTO", "ABSTENÇÃO"] & turno == 1')

data['votos'] = pd.to_numeric(data['votos']) # If u don't cast it to integer it GETS CRAZZZZYYYYYYY
sumarioGeral = data.groupby(['situacao', 'ano', 'turno'])['votos'].agg('sum')

sumarioGeral.to_csv('comparecimento.csv', header=True)