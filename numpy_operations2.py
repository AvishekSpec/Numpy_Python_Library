import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a)

b=np.linspace(5,10,15)
print(b)

#using reshape operation to make 3 columns and 2 rows
a=a.reshape(3,2)
print(a)

#using slicing operation 
print(a[0:, 2]) 