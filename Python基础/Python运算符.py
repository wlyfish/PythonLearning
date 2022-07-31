# _*_ coding:utf-8 _*_
# @time 2022/6/29 22:39
# @Author wly
# @name Python运算符.py
print([1, 2] + [3, 4] + [5, 6])

print(3 ** 10)

print(5 / 2)
print(5 // 2)
print(type(5 // 2))

print(5.2 / 2)
print(5.2 // 2)
print(type(5.2 // 2))

# print(1 / 0)

print(5 > 2)
print(type(5 > 2))

result = 10 != 10
print(result)

num = 10
print(id(num))
b = 10
print(id(b))
print(num is b)

c = [1]
d = [1]
print((c == d))
print(id(c), id(d))
print(c is d)

bool1 = True
print(not bool1)

num4 = 1
# print(False and num4)
print(1 or False)

print(0 and True)

print(1 and 4)
