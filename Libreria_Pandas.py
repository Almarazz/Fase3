import pandas as pd
import numpy as np

s= pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
s.count()
print(s.count())

s.sum()
print(s.sum())

s.cumsum()
print(s.cumsum())

s.value_counts()
print(s.value_counts())

s.value_counts(normalize=True)

s.min()
print(s.min())


s.max()
print(s.max())

s.mean()
print(s.mean())

s.std()
print(s.std())


s.describe()
print(s.describe())


import pandas as pd

s = pd.Series([1, 2, 3, 4])
s*2
print(s)

s%2
print(s)

s = pd.Series(['a', 'b', 'c'])
s*5
print(s)


from math import log
s = pd.Series([1, 2, 3, 4])
s.apply(log)
print(s.apply(log))

s = pd.Series(['a', 'b', 'c'])
s.apply(str.upper)
print(s.apply(str.upper))

s = pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Programacion': 8.5})
print(s[s > 5])

s = pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Programacion': 8.5})
print(s.sort_values())

print(s.sort_index(ascending = False))


s = pd.Series(['a', 'b', None, 'c', np.NaN, 'd'])
s
print(s)

s.dropna()
print(s.dropna())

datos = {'nombre': ['Maria', 'Luis', 'Carmen', 'Antonio'],
         'edad': [18, 22, 20, 21],
         'grado': ['Economia', 'Medicina', 'Arquitectura', 'Economia'],
         'correo': ['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
         }
df = pd.DataFrame(datos)
print(df)


df = pd.DataFrame([['Maria', 18], ['Luis', 22], ['Carmen', 20]], columns = ['Nombre', 'Edad'])
print(df)


df = pd.DataFrame([{'Nombre': 'Maria', 'Edad': 18}, {'Nombre': 'Luis', 'Edad': 22}, {'Nombre': 'Carmen'}])
print(df)


df = pd.DataFrame(np.random.randn(4, 3), columns = ['a', 'b', 'c'])
print(df)


df = pd.read_csv(
'https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesteroles.csv', sep=';',
decimal=',')
print(df.head())


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
df.info()

df.shape()
df.size()
df.columns()
df.index()
df.dtypes()


df = pd.read_csv(
'https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.rename(columns={'nombre':'nombre y apellidos', 'altura':'estatura'}, index={0:1000, 1:1001, 2:1002}))


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.reindex(index=[4, 3, 1], columns=['nombre', 'tensión', 'colesterol']))


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.iloc[1, 3])

print(df.iloc[1, :2])


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.loc[2, 'colesterol'])

print(df.loc[:3, ('colesterol','peso')])

print(df['colesterol'])


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
df['diabetes'] = pd.Series([False, False, True, False, True])
print(df)


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df['altura']*100)

print(df['sexo']=='M')


from math import log

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df['altura'].apply(log))


df = pd.DataFrame({'Name': ['María', 'Carlos', 'Carmen'], 'Nacimiento':['05-03-2000', '20-05-2001', '10-12-1999']})
print(pd.to_datetime(df.Nacimiento, format = '%d-%m-%Y'))


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.describe())


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
edad = df.pop('edad')
print(df)


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
df = df.append(pd.Series(['Carlos Rivas', 28, 'H', 89.0, 1.78, 245.0], index=['nombre','edad','sexo','peso','altura','colesterol']), ignore_index=True)
print(df.tail())


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.drop([1, 3]))


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df[(df['sexo']=='H') & (df['colesterol'] > 260)])


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.sort_values('colesterol'))


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.dropna())


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.groupby('sexo').groups)

print(df.groupby(['sexo','edad']).groups)


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.groupby('sexo').get_group('M'))


df = pd.read_csv('https://raw.githubusercontent.com/asalber/manualpython/master/datos/colesterol.csv')
print(df.groupby('sexo').agg(np.mean))


datos = {'nombre':['María', 'Luis', 'Carmen'], 'edad':[18, 22, 20], 'Matemáticas':[8.5, 7, 3.5], 'Economía':[8, 6.5, 5], 'Programación':[6.5, 4, 9]}
df = pd.DataFrame(datos)
df1 = df.melt(id_vars=['nombre', 'edad'], var_name='asignatura', value_name='nota')
print(df1)

print(df1.pivot(index='nombre',
columns='asignatura', values='nota'))