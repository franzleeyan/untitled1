import base64

# from io import BytesIO

# python3版本
str2 = "Q0h1YXdlaV80MDA0NDAwMDAwMDA5ODQ0Nw=="
binIO = BytesIO()
binIO.write(str2.encode("utf-8"))
encodeTest = BytesIO()
decodeTest = BytesIO()
# 对BytesIO内的数据进行编码
binIO.seek(0)
base64.encode(binIO, encodeTest)
print(encodeTest.getvalue())
# 对BytesIO内的数据进行解码
encodeTest.seek(0)
base64.decode(encodeTest, decodeTest)
print(decodeTest.getvalue())
