import numpy as np 

print('------- 1 -------')
np.random.seed(5)
quest1 = np.random.rand(10)
print(quest1)
quest1 = 100 * quest1
print(np.floor(quest1))

print('\n------- 2 -------')
np.random.seed(10)
quest2 = np.random.randint(1, 51, size=(4, 4))
print(quest2)

print('\n------- 3 -------')
linhas = quest2.sum(axis=1)/4
print("Média linha:", linhas)
colunas = quest2.sum(axis=0)/4
print("Média coluna:", colunas)
print("Maior valor linhas:", np.max(linhas))
print("Maior valor colunas:", np.max(colunas))

print('\n------- 4 -------')
flat_quest2 = quest2.flatten()
numeros, frequencias = np.unique(flat_quest2, return_counts=True)
print("Numeros:", numeros)
print("Frequência:", frequencias)
quest4 = numeros[frequencias == 2]
print("Números que aparecem 2 vezes:", quest4)