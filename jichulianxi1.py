# bicycles = ['trek','cannondale','red','specializde']
# message = 'My first bicycle was a ' + bicycles[0].title() + '。'
# print(bicycles)
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[1].title())
# print(bicycles[3].title())
# print(bicycles[-1])
# print(message)

# 试一试
# 定义名字
# name= ['诺涵','小明','小强','小齐','小芳']
# message1 = name[0] +'，' '你好!'
# message2 = name[1] +'，' '你好!'
# message3 = name[2] +'，' '你好!'
# message4 = name[3] +'，' '你好!'
# message5 = name[4] +'，' '你好!'

# print(name)
# print(message1)
# print(message2)
# print(message3)
# print(message4)
# print(message5)

# bicycles = ['audi a3 car','honda motorcycle','gongxiang bike','ditie']
# message = 'I would like to own a '+ bicycles[0].title() +'。'
# print(bicycles)
# print(message)

# motorcycles = ['honda','yamaha','suzuki']
# motorcycles[0] = 'ducati'
# motorcycles.append('ducati')
motorcycles = []
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')

print(motorcycles)
# motorcycles.insert(0,'ducati')
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
# last_owned = motorcycles.pop()
# print('The last motorcycle I owned was ' + last_owned.title() + '。')
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was ' + first_owned.title() + '。')
# motorcycles.remove('ducati')
# print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')