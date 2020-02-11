# magicians = ['alice','david','carolina']
# for magicians in magicians:
#     # print(magicians)
#     print(magicians.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick," + magicians.title() + ".\n")
#
# print("Thank you, everyone. That was great magic show!")

'''
作业
    1、用for打印出3个披萨的名字
    2、修改这个for的循环，使其打印包含披萨名字的语句，而不仅仅是披萨的名称，对于每个披萨，都显示一行输出
    3、程序末端加入一行代码，她不在for循环中
'''
# Pizza = ['Bigger','Pizzahut','Domino']
# for Pizza in Pizza:
#     print(Pizza.title() + ", that was a good food!")
#
# print("But i like chinese food")

# name = 'dongGe'
# for x in name:
#     print('----')
#     if x == 'g':
#         break
#     print(x)

name = 'dongGe'
for x in name:
    print('----')
    if x == 'g':
        continue
    print(x)

# name = 'Hello'
# for x in name:
#     print('----')
#     print(x)
#     # if x =='l':
#     #     break
# else:
#     print("==for循环过程中，如果没有break则执行==")

# i = 0
# while i < 10:
#     i = i+1
#     print('----')
#     if i==5:
#         break
#     print(i)