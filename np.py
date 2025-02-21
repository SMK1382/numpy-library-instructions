import numpy as np
# a = np.array(["reza", 2.2, 3, 4, 5])
# a = np.arange(0, 15, 2)
# a = np.linspace(0, 20, 8, retstep = True)
# a = np.linspace(0, 20, 8)
# a = np.ones((2, 3, 4), dtype = int) # == np.zeros((2, 3, 4), dtype = int)
# a = np.random.random(size = (3, 4))
# np.random.seed(1)
# a = np.random.randint(1, 10, size = (3, 4), dtype = int)
# print("a.shape: ", a.shape)
# print("a.ndim: ", a.ndim)
# print("a.dtype: ", a.dtype)
# a.shape = (1, 5)
# print("a: ", a)
######################################################################
# b = np.arange(1, 21)
# b.shape = (4, 5)
# print(b)
# print(b[: , :2])
######################################################################
# a = np.arange(1, 61)
# a = a.reshape(1, 60)
# a.shape = (1, 60)
# a.shape = (60)
# print(a)
######################################################################
# Masked Array
# a = np.random.randint(1, 10, size=(60))
# unique = np.unique(a)
# print(unique)
# print(a[ a > 3])
# greater_than_30 = a > 3
# print(greater_than_30)
# even_elements = a % 2 == 0
# print(even_elements)
# final_mask = a > 3 and a % 2 == 0
# a.shape = (1, 60)
# print(a)
######################################################################
# structured
# names = ['ali', 'mohammadreza', 'reza']
# ages = [25, 22, 20]
# cities = ['tehran', 'mashhad', 'shiraz']
# patterns = [('name', 'U20'), ('age', 'i4'), ('city', 'U20')]
# my_array = np.zeros((3), dtype = patterns, )
# # my_array[0] = (names[0], ages[0], cities[0])
# my_array[0], my_array[1], my_array[2] = (names[0], ages[0], cities[0]), (names[1], ages[1], cities[1]), (names[2], ages[2], cities[2])
# print(my_array)
# print("****************************")
# # my_array.shape = (1, 3)
# # print(my_array.shape)
# print(my_array['age'])
######################################################################
# view 
# first_array = np.arange(1, 25)
# second_array = first_array.view() # np.copy(first_array)
# second_array = np.copy(first_array)
# first_array[0] = 1000
# print(first_array)
# print("*****************")
# print(second_array)
# print(second_array is first_array)
######################################################################
# np.random.seed(1)
# x = np.random.randint(1, 100, size=5)
# x = np.random.random((3, 4))
# x = np.ones((2, 3, 4))
# print(x)
######################################################################
# append
# np.random.seed(1)
# x = np.random.randint(1, 100, size=5, dtype=int)
# x = np.ones((3, 4, 5), dtype=int)
# y = np.zeros((2, 4, 5), dtype=int)
# # x = np.append(x, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], axis=0)
# x = np.append(x, y, axis=0)
# print(x)
######################################################################
# insert
# np.random.seed(1)
# x = np.ones((3, 4), dtype=int)
# # x = np.insert(x, 0, [10, 11, 12, 13], axis=0)
# x = np.insert(x, 0, [10, 11, 12], axis=1)
# print(x)
######################################################################
# empty
# a = np.empty((3,4))
# print(a)
######################################################################
# delete
# np.random.seed(0)
# a = np.random.randint(1, 100, size=20).reshape(4, 5)
# print(a)
# print("********************")
# a = np.delete(a, 0, axis=1)
# print(a)
######################################################################
# concat
# np.random.seed(0)
# a = np.random.randint(1, 10, size=12).reshape(3, 4)
# b = np.random.randint(1, 10, size=12).reshape(3, 4)
# print(a)
# print("*******************")
# print(b)
# print("*******************")
# result = np.concatenate((a, b), axis=1)
# print(result)
######################################################################
# stack
# np.random.seed(0)
# a = np.random.randint(1, 100, size=10).reshape(2, 5)
# b = np.random.randint(1, 100, size=10).reshape(2, 5)
# print("array a:")
# print(a)
# print("array b:")
# print(b)
# print("***************************")
# print(np.stack((a, b), axis=0))
# print("***************************")
# print(np.stack((a, b), axis=1))
# print("***************************")
# print(np.stack((a, b), axis=2))
# print(np.stack((a, b), axis=2).shape)
######################################################################
# split
# np.random.seed(0)
# a = np.random.randint(1, 100, size=40).reshape(4, 2, 5)
# print(a)
# print("***************************")
# print(np.split(a, 2, axis=0))
# print("***************************")
# print(np.split(a, 2, axis=1))
# print("***************************")
# print(np.split(a, 1, axis=2))
######################################################################
# ravel
# a = np.random.randint(1, 100, size=10).reshape(2, 5)
# result = np.ravel(a)
# print(result)
# print(a)
######################################################################
# flatten
# x = np.arange(20)
# y = list(map(int, x.flatten()))
# y = x.flatten()
# x[0] = 1234
# print(x is y)
# print("x:\n", x)
# print("y:\n", y)
# for i in y:
#     print(i)
######################################################################
# flat
# x = np.arange(20)
# y = x.flat
# x[0] = 1234
# print("x:\n", x)
# print("y:\n", y)
######################################################################
# Convert numpy to list
# x = np.arange(20)
# y = list(map(int, x.flat))
# x[0] = 1234
# print(list(x.flat))
# print(x)
# print(y)
# print(x.tolist())
# print(x)
######################################################################
# fliplr
# x = np.arange(24).reshape(2, 3, 4)
# x = np.fliplr(x)
# print(x)
######################################################################
# flipud
# x = np.arange(24).reshape(2, 3, 4)
# x = np.flipud(x)
# print(x)
######################################################################
# roll
# x = np.arange(24).reshape(2, 3, 4)
# print(np.roll(x, -5))
######################################################################
# rot90
# x = np.arange(24).reshape(2, 12)
# print(x)
# print(np.rot90(x))
# print(np.rot90(x, k=-1))
######################################################################
# transpose
# x = np.arange(24).reshape(2, 3, 4)
# print("x:")
# print(x)
# print("*******************************************************")
# print("x transpose:")
# print(np.transpose(x, axes=(2, 0, 1)))
######################################################################
# swapaxes == transpose
# x = np.arange(24).reshape(2, 3, 4)
# print(x)
# print("*****************************************************************")
# print(np.transpose(x, axes=(2, 1, 0)))
# print("*****************************************************************")
# print(np.swapaxes(x, 0, 2))
# print("((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))")
######################################################################
# moveaxis
# x = np.arange(24).reshape(2, 3, 4)
# print("x:") 
# print(x) 
# print("*******************************************************************")
# print(np.moveaxis(x, 2, 0))
# print(np.moveaxis(x, 2, 0).shape)
######################################################################
# dot product
# x = np.random.randint(0, 100, size=(3, 4))
# y = np.random.randint(0, 100, size=(4, 3))
# z = np.dot(x, y)
# print(x)
# print("*******************************************************************")
# print(y)
# print("*******************************************************************")
# print(z)
######################################################################
# tile
# x = np.arange(10).shape(2, 5)
# print(np.tile(x, 3))
# print(np.tile(x, (3, 2, 1)))
######################################################################
# repeat
# x = np.arange(10).reshape(2, 5)
# print(np.repeat(x, 2, axis=(0)))
######################################################################
# sort
# x = np.random.randint(100, size=10).reshape(2, 5)
# print(x)
# print("**************")
# print(np.sort(x, axis=(0)))
######################################################################
# argsort
# x = np.random.randint(100, size=10).reshape(2, 5)
# print(x)
# print("***********************************")
# print(np.argsort(x))
######################################################################
# argmax and argmin
# x = np.random.randint(100, size=10)
# print(x)
# print(np.argmax(x))
# print("***********")
# print(np.argmin(x))
######################################################################
# frompyfunc
# def squar(x):
#     return x ** 2
#
# np_func = np.frompyfunc(squar, 1, 1)
#
# z = np.arange(20)
# print(z)
# print("********************")
# print(np_func(z))
######################################################################
# outer
# x = np.arange(10)
# y = np.arange(10, 20)
# print(np.outer(x, y))
