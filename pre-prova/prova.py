import numpy as np 

arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

print('-------- 1 --------')
quest1 = arr[:, :4]
print(quest1)

print('-------- 2 --------')
Region = np.unique(arr[:,1])
print(Region)
print("total de regioes unicas",Region.shape[0])

print('-------- 3 --------')
dados = arr[1:,9].astype(float)
quest3 = np.mean(dados)
print("Média:", quest3)

print('-------- 4 --------')
dados = arr[1:]
paises = dados[:,1]
paises = np.char.strip(paises)
quest4 = np.count_nonzero(np.char.find(paises, 'NORTHERN AMERICA') != -1)
print("Países da america do norte:", quest4)

print('-------- 5 --------')
paises = arr[arr[:, 1] == 'LATIN AMER. & CARIB    ']
print(paises)
GDP = paises[1:,8].astype(float)
GDP = np.max(GDP)
paises = paises[paises[:, 8].astype(float) == GDP]
print('GDP: ', GDP)
print('paises: ', paises)
