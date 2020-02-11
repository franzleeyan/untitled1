# 读取一个文件


import base64
c = "Q0h1YXdlaV80MDA0NDAwMDAwMDA5ODQ0Nw=="
# b =base64.b64encode(payload.encode('utf-8')).decode("utf-8")
# print(b)
# 'Q0h1YXdlaV80MDA0NDAwMDAwMDA5ODQ0Nw=='
encoded = base64.b64decode(c)
print(encoded)
# 'select * from workbasic'

