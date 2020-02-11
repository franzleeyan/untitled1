a = 10
a += 1 # a = a + 1
print(a)

b = 10
b -= 1 # b = b - 1
print(b)

c = 10
c *= 1 # c = c * 1
print(c)

# 注意：先算复合赋值运算符右侧的表达式；再算复合赋值运算
d = 10
# d = 10 + 1 + 2
# d += 3 -- d = d + 3
d += 1 + 2
print(d)

e = 10
e *= 1 + 2
print(e)