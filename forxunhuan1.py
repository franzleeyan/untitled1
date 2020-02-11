name = 'dongGe'
for x in name:
    print(x)


name = 'hello'
for x in name:
    print(x)
    if x =='l':
        break   # 退出for循环
else:
    print("==for循环过程中，如果没有break则执行==")