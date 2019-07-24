#第十个练习 - 猜数字游戏

#生成一个随机数需要用到random
import random
a = random.randint(1,100)
print("-------猜数字游戏-------")
b = int(input("请输入1～100之间的任一个数（退出游戏请输入-1）：\n"))
while b != a:
    if b == -1:
        break
    elif b < a:
        b = int(input("太小，请重新输入：\n"))
        continue
    else:
        b = int(input("太大，请重新输入：\n"))
        continue
if b == a:
    print("恭喜你，你赢了，猜中的数字是：" + str(b))
print("--------游戏结束-------")

#改用for循环实现
'''
import random
a = random.randint(1,100)
print("-------猜数字游戏-------")
b = int(input("请输入1～100之间的任一个数（退出游戏请输入-1）：\n"))
for i in range(1,10000):#为防止有人一直猜一个数，因此将范围定的尽量大
    if b == -1:
        break
    elif b == a:
        print("恭喜你，你赢了，猜中的数字是：" + str(b))
        break
    elif b < a:
        b = int(input("太小，请重新输入：\n"))
        continue
    else:
        b = int(input("太大，请重新输入：\n"))
        continue
print("--------游戏结束-------")
'''