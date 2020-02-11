'''
1. 出拳
    玩家：手动输入
    电脑：1. 固定：剪刀；2. 随机
2. 判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
'''
# 导入模块在最上面
import random

# 1.出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布:'))
computer = random.randint(0, 2)
# 电脑输入 print(computer)
# 2.判断输赢
# 玩家获胜
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print(f'您输入的是{player},电脑给出的是{computer},玩家获胜，祝贺您')
# 平局
elif player == computer:
    print(f'您输入的是{player},电脑给出的是{computer},平局，别走，再来一局')
# 电脑获胜
else:
    print(f'您输入的是{player},电脑给出的是{computer},实在抱歉，电脑获胜')
print('本局结束')