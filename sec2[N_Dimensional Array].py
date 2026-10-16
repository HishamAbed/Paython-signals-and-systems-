# print("numpy")

# my_list = [1, 2, 3, 4, 5] # we can create a list in python using [] brackets , we can change the values of list after creating it
# print(my_list)
# print(type(my_list))

# my_tuple = (1, 2, 3, 4, 5) # we can create a tuple in python using () brackets , we cannot change the values of tuple after creating it
# print(my_tuple) 
# print(type(my_tuple))

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))           # ndarray -->    N_ dimensional array
print(arr*2)
print(arr.ndim)
# we can convert list and tuple to numpy array --> array() function is used to convert list and tuple to numpy array
# arr = np.array(my_list)   ,  arr = np.array(my_tuple)  ,  arr = np.array([1, 2, 3, 4, 5])   are all same

# 0D --> scalar array
print("0D array")
arr2=np.array(42)
print(arr2)
print(arr2.ndim)

#-------------------------------------------------------------------
print("--------------------------------------")
#1D --> 1 dimensional array
print
arr3=np.array([1,2,3,4,5])
print(arr3)
print(arr3.ndim)
print(arr3[0])   # indexing

#-------------------------------------------------------------------
# 2D --> 2 dimensional array  صفوف واعمدة
print("--------------------------------------")
print("2D array")
arr4=np.array([[1,2,3],[4,5,6]])
print(arr4)
print(arr4.ndim)
print(arr4[0,1])   # indexing   0 --> row index, 1 --> column index

#-------------------------------------------------------------------
# 3D --> 3 dimensional array
print("--------------------------------------")
print("3D array")
arr5=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr5)
print(arr5.ndim)
print(arr5[0,1,2])   # indexing   0 --> 1st array, 1 --> 2nd row, 2 --> 3rd column