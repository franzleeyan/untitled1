a = 0
b = 1
c = 2

# 1. and: 与： 都真才真
print(a < b and c > b)
print(a > b and b < c)

# 2. or: 或： 一真则真，都假才假
print(a < b or c > b)
print(a > b or b < c)
print(a > b or b > c)
print(a > c or b > c)

# 3. not: 非： 取反
print(not False)
print(not c > b)
print(not True)
print(not a > b)