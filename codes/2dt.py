# translation

import numpy as np

#size = map(int,input('Enter the number of co-ordinates:'))
mat = np.zeros(6,dtype = 'int').reshape(3,2)

print('Enter the co-ordinates')
for i in range(0,3):
        x,y = (map(int,input().split()))
        mat[i][0] = x
        mat[i][1] = y
        
print('The matrix you entered is:')
print(mat)
    
print('Enter the translation paramater:')
t = int(input())

print('The matrix after translation is:')
print(mat + (t * mat))

