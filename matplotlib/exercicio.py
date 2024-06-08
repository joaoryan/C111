import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = '/home/joao/Workspace/Inatel 2024/C111-Analise-de-Dados/matplotlib/space.csv'
dfSpace = pd.read_csv(file_path, delimiter=';')
empresas_eua = dfSpace[dfSpace['Location'].str.contains('USA')]
empresas_china = dfSpace[dfSpace['Location'].str.contains('China')]
num_empresas_eua = len(empresas_eua)
num_empresas_china = len(empresas_china)
num_empresas = [num_empresas_eua, num_empresas_china]
plt.bar(['EUA', 'China'], num_empresas, color=['blue', 'red'])
plt.title('Número de Empresas Espaciais nos EUA e na China')
plt.show()

