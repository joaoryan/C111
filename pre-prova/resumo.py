import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# ordenar array
arr.sort()

print('-------- 1 --------')
# arr[LI:LF, CI:CF]
quest1 = dataset[:, :4]

print('-------- 2 --------')
# np.unique - pega apenas valores unicos
Region = np.unique(dataset[:,1])
# shape[0] - mostra a dimensão do array
Region.shape[0]

print('-------- 3 --------')
# astype(float) - converte para float
dados = dataset[1:,9].astype(float)
# calcula media
quest3 = np.mean(dados)

print('-------- 4 --------')
# exclui a primeira linha 
dados = dataset[1:]
# pega a coluna da segunda coluna de indice 1
paises = dados[:,1]
# remove espaço em branco
paises = np.char.strip(paises)
# np.char.find(paises, 'NORTHERN AMERICA') != -1) retorna true se encontrar e false caso não encontre
# np.count_nonzero conta o número de valores True no array.
quest4 = np.count_nonzero(np.char.find(paises, 'NORTHERN AMERICA') != -1)

print('-------- 5 --------')
# seleciona todas linhas em que a coluna 2 indice 1 tem nome 'LATIN AMER. & CARIB    '
paises = dataset[dataset[:, 1] == 'LATIN AMER. & CARIB    ']
# tranforma coluna 9 indice 8 float
GDP = paises[:,8].astype(float)
#pega valor maximo
GDP = np.max(GDP)
# Pega pais em que a coluna de indice 8 possui valor igual max
paises = paises[paises[:, 8].astype(float) == GDP]
