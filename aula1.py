# TUPLAs
print('------ TUPLA ------')
# coleção imutavel
nomes = ('goku', 'vegeta', 'trunks', 'gohan')
# slicing de dados, serve para dividir os dados
print(nomes[0]) 
print(nomes[:2]) 
print(nomes[1:3]) 
print(nomes[:2]) 
print(nomes[-2]) 
#update não e possivel pois e imutavel
#nomes[0] = 'bulma'

# LISTA
print('------ LISTA ------')

nomes = ['goku', 'vegeta', 'trunks', 'gohan']
#add
nomes.append('bulma')
#update
nomes[0] = 'goten'
#delete
nomes.remove('trunks')
del nomes[2]
#select
print(nomes)

# SETS
#não quarda ordem dos elementos
print('------ SETS ------')
nomes = {'goku', 'vegeta', 'trunks', 'gohan'}
#add
nomes.add('bulma')
nomes.add('goku') #não guarda elementos repetidos
print(nomes)
# remover
nomes.remove('gohan')
# update (gambiarraaa)
nomes.remove('goku')
nomes.add('goku-edit')
print(nomes)

# DICIONARIOS
# indices customizaveis
print('------ DICIONARIOS ------')
pessoa = {'nome': 'goku', 'idade': 97}
pessoa2 = {'nome': 'bulma', 'idade': 16}
#add
pessoa['sexo'] = 'M'
#update
pessoa['nome'] = 'goten'
#delete
del pessoa['idade']
print(pessoa)

#COLEÇOES ANINHADAS
print('------ COLEÇOES ANINHADAS ------')
nomes=[pessoa, pessoa2]
print(nomes[1]['nome'])


