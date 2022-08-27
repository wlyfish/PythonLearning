# _*_ coding:utf-8 _*_
# @time 2022/8/27 16:41
# @Author wly
# @name Numpy-mean.py
import numpy as np

a = np.array([[1., 2.], [3., 4.]])
# print(a)
# print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

num1 = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
print(num1)
num2 = np.mat(num1)
print(num2)

print(np.mean(num2))

print(np.mean(num2, 0))
print(np.mean(num2, 1))
