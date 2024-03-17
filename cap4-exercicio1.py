import numpy as np 

array1 = np.linspace(0, 1, 21)
print('------- 1 -------')
print("1:", array1)

array2 = np.arange(0, 52, 2)
array3 = np.arange(100, 48, -2)
concatenado = np.concatenate((array2, array3))
concatenado.sort()
print('------- 2 -------')
print("2:", concatenado)

decrescente = np.flip(np.sort(concatenado)) 
print('------- 3 -------')
print("3:", decrescente)

matriz = np.ones((3, 4))
array1D = matriz.flatten()
print('------- 4 -------')
print("4:", matriz)
print("4:", array1D)

matrizQualquer = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linhas, colunas = matrizQualquer.shape
totalElementos = linhas * colunas
print('------- 5 -------')
if totalElementos % 2 == 0:
    print("5: A matriz pode se um vetor com número par")
else:
    print("5: A matriz pode se um vetor com número ímpar")