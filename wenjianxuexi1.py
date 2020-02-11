# f = open('test.txt','w')
# f .write('hello world，I am here！')
# f .close()

# f = open('test.txt','r')
# content = f.read(5)
# print(content)
# print("-"*30)
# content = f.read()
# print(content)
# f.close()

# coding = utf-8
# f = open('test.txt','r')
#
# content = f.readlines()
#
# print(type(content))
#
# i = 1
# for temp in content:
#     print("%d:%s"%(i, temp))
#     i+=1
#
# f.close()

# coding = utf-8
f = open('test.txt','r')
content = f .readline()
print("1:%s"%content)
content = f .readline()
print("2:%s"%content)

f .close()