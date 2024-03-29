import numpy as np 

arr = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
print('------- 1 -------')
total = arr.shape[0]
sucesso = np.count_nonzero(arr[:, -1] == 'Success')
quest1 = (sucesso / total) * 100
print(f'A porcentagem é {quest1}%')

print('\n------- 2 -------')
dados = arr[1:]
gastos = dados[:, -2].astype(float)
quest2 = np.mean(gastos[gastos > 0])
print("Média de gastos:", quest2)

print('\n------- 3 -------')
dados = arr[1:]
localizacao = dados[:, 2]
quest3 = np.count_nonzero(np.char.find(localizacao, 'USA') != -1)
print("Número de missões EUA:", quest3)

print('\n------- 4 -------')
dados = arr[1:]
spacex = dados[dados[:, 1] == 'SpaceX']
custo = spacex[:, -2].astype(float)
indiceMax = np.argmax(custo)
quest4= spacex[indiceMax]
print("Missão mais cara:", quest4)

print('\n------- 5 -------')
dados = arr[1:]
empresas = {}
for linha in dados:
    empresa = linha[1]
    if empresa in empresas:
        empresas[empresa] += 1
    else:
        empresas[empresa] = 1

for empresa, quantidade in empresas.items():
    print("Empresa", empresa, "possui", quantidade, "de missões")