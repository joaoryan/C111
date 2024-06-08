import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset as pds

file_path = '/home/joao/Workspace/Inatel 2024/C111-Analise-de-Dados/matplotlib/paises.csv'

# scatter plot(grafico de dispersão)
dfPaises = pd.read_csv(file_path, delimiter=';')
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')
plt.scatter(dfPaises2['Country'], dfPaises2['GDP ($ per capita)'], s=dfPaises2['Area (sq. mi.)']/10000)
plt.show()

# bar plot(grafico em barras)
df = pd.DataFrame(pds.data('HairEyeColor'))
grupoCorCabelo = df.groupby('Hair').sum()
plt.bar(grupoCorCabelo.index.values, grupoCorCabelo['Freq'], color='green')
plt.show()

file_path = '/home/joao/Workspace/Inatel 2024/C111-Analise-de-Dados/matplotlib/space.csv'
dfSpace = pd.read_csv(file_path, delimiter=';')
dfRosc = dfSpace[dfSpace['Company Name'].str.contains('Roscosmos')]
falha = len(dfRosc[dfRosc['Status Mission'].str.contains('Failure')])
sucesso = len(dfRosc[dfRosc['Status Mission'].str.contains('Success')])
plt.pie(
    x=[sucesso, falha], 
    labels=['Missoes com sucesso', 'Missoes que falharam'], 
    shadow=True, 
    explode=[0, 0.2], 
    autopct='%1.1f%%'
)
plt.title('Status Missoes')
plt.show()
