# 基础练习 作业1
"""
1、建立空名单
2、向名单中添加邀请人员
3、打印邀请人员参加宴会
"""
YAOQINGRENYUAN = []
YAOQINGRENYUAN.append('小涵')
YAOQINGRENYUAN.append('小齐')
YAOQINGRENYUAN.append('小乐')
print(YAOQINGRENYUAN)
MASSAGE0 = YAOQINGRENYUAN[0] + '你好，邀请你参加今晚的宴会。'
MASSAGE1 = YAOQINGRENYUAN[1] + '你好，邀请你参加今晚的宴会。'
MASSAGE2 = YAOQINGRENYUAN[2] + '你好，邀请你参加今晚的宴会。'

print(MASSAGE0)
print(MASSAGE1)
print(MASSAGE2)

# 基础练习 作业2
var = ("\n"
       "    1、使用上面的名单\n"
       "    2、名单中有人无法参加，需要加入原因\n"
       "    3、用新的邀请人替换名单中的人\n"
       "    4、向新的邀请名单人员，发出邀请\n")

# 无法参加的人员名单存储到无法参加中，原因为有事无法参加
BUSY_NAME = '小涵'
YAOQINGRENYUAN.remove(BUSY_NAME)
print(YAOQINGRENYUAN)
print("很抱歉，" + BUSY_NAME.title() + "由于有事情，无法参加宴会。")
YAOQINGRENYUAN.append('小媛')
MASSAGE0 = YAOQINGRENYUAN[0] + '你好，邀请你参加今晚的宴会。'
MASSAGE1 = YAOQINGRENYUAN[1] + '你好，邀请你参加今晚的宴会。'
MASSAGE2 = YAOQINGRENYUAN[2] + '你好，邀请你参加今晚的宴会。'

print(MASSAGE0)
print(MASSAGE1)
print(MASSAGE2)

('\n'
 '1. 由于发现了更大的桌子，还需要邀请三位嘉宾\n'
 '2. 使用上面的名单，并在最后写出我们有了更大的桌子，可以邀请更多的人员参加\n'
 '3. 添加新邀请的名单：\n'
 '    3.1 使用insert 将一位新嘉宾添加到名单开头\n'
 '    3.2 使用insert 将另一位嘉宾添加到名单中间\n'
 '    3.3 使用append 将最后一位嘉宾名单添加到名单末尾\n'
 '4. 打印一系列消息，向名单中的每位嘉宾发出邀请\n')

print('各位，由于我们找到了一个更大的餐桌，因此我们再次邀请三位参加我们的宴会。')
