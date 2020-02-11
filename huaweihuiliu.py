# 调用base64解码
import base64

# 定位文件名称
oldFileName = 'test.txt'
text=""   # 增加一个空字符

with open(oldFileName) as file_object:
    for line in file_object:
#        print(line.rstrip())
# 解码其中的64位代码
        b = base64.b64decode(line.rstrip())
        # print(b)
# 从byte转换为str
        c: str = b.decode()
# 输出str内容
        print(c)
        text=text+ c +"\n\r"
# 写入文件
ms = open('out.txt')
with open('out.txt','w') as mon:
    mon.write(text.strip('\n'))
# 解决空行问题
# f = open('out.txt')
# logs = f.read().splitlines()
# for log in logs:
#     print(log)
# f.close()
# print(logs)









# # 提取文件的后缀
# fileFlagNum = oldFileName.rfind('.')
# if fileFlagNum > 0:
#     fileFlag = oldFileName[fileFlagNum:]
# # 组织新的文件名字
# newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag
#
# # 创建新文件
# newFile = open('test[复件].txt','w')
#
# # 把就文件中的数据，一行一行的进行写入到新文件中
# for lineContent in oldFile.readlines():
#     newFile.write(lineContent)
#
# # 关闭文件
# oldFile.close()
# newFile.close()