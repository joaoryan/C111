# 1
print('--------- 1 ---------')
times = ['real madrid', 'bota fogo', 'vasco', 'barcelona', 'porto']

#a
print('a)')
print(times[:3])
#b
print('b)')
print(times[-2:])
#c
print('c)')
times.sort()
print(times)
#d
print('d)')
print(times.index("barcelona"))

# 2
print('--------- 2 ---------')

loja1 = {'iphone', 'xiaomi', 'nokia'}
loja2 = {'samsung', 'xiaomi', 'motorola', 'nokia'}

modelos = loja1 | loja2

print("Todos os modelos:")
for modelo in modelos:
    print(modelo)

modelosAmbasLojas = loja1 & loja2

print("Ambas as lojas:")
for modelo in modelosAmbasLojas:
    print(modelo)


# 3
print('--------- 3 ---------')

nome = input('digite nome do aluno: ')
media = float(input('digite a media do aluno: '))

aluno = {'nome': nome, 'media': media}

status = ''
if(media >= 60): status = 'AP' 
else: status = 'RP'
  
print('situação atual do aluno:', status)
aluno['status'] = status
print(aluno)
