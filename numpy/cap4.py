import numpy as np 

'''
#NumPy Array
print('--------- 1-D ----------')
#1 - D
arr = np.array([2,3,1])
print(arr)
print(type(arr))
arr = np.sort(arr)
print(arr)

print('--------- 2-D ----------')
#2 -D
mtz = np.array([[1,2], [3,4]])
print(mtz)

print('--------- estruturando array ----------')
print('--- ones ---')
mtz = np.ones([5, 5])
print(mtz)

print('--- zeros ---')
arr = np.zeros(10)
print(arr)

print('--- arange ---')
arr = np.arange(20,30,1).reshape(5,2)
print(arr)
'''

#Operaçoes NumPy arrays

jan = np.arange(20, 30, 1)
fev = np.arange(40, 50 , 1)
print(jan)
print(fev)
print(jan + fev)
print(np.concatenate([jan, fev]).reshape(5, 4))

print(jan.size)
print(jan.ndim)
print(jan.shape)

