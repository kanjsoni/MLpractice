import numpy as np
from time import process_time

python_list = [i for i in range (100000)]
start_time = process_time()
python_list = [i+5 for i in python_list]
end_time = process_time()
print(end_time - start_time)

np_array= np.array([i for i in range (100000)])
start_time = process_time()
python_list = [i+5 for i in python_list]
end_time = process_time()
print(end_time - start_time)

list1 = [2,4,5,7,3]
print(list1)
type(list1)

np_array = np.array([2,4,5,7,3])
print(np_array)
print(type(np_array))

#creating 1d array 

a= np.array([1,2,3,4])
print(a)
print(a.shape)

#creating 2d array

# b = np.array([1,2,4,5],[4,6,3,5])
# print(b)
# print(b.shape)


#declaring floatng type value

c= np.array([1,3,5,5,6], [4,5,1,6,6] ,dtype=float)


#initial placeholders in numpy arrays

#creating a numpy of zeros

x= np.zeros((4,5))
print(x)

#creating a numpy of ones

y= np.ones((3,3))

z = np.full((3,4),5)
print(z)

#creating an identity matrix

a1 = np.eye(5)
print(a1)

#creating a numpy with random value

b1= np.random.random((3,4))
print(b1)
