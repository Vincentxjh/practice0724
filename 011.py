#第十一个练习 - 模拟“跳一跳”小游戏加分块

print("----------跳一跳----------")
print("欢迎回来，请开始游戏……")
print("请输入中心、音乐块、微信支付块（退出程序请输入“退出”）：")
judge = True
while judge:
    name = input("请输入：\n")
    if name == "中心":
        print("您的分数为：32")
    elif name == "音乐块":
        print("您的分数为：30")
    elif name == "微信支付块":
        print("您的分数为：42")
    elif name == "退出":
        print("已退出，再见！")
        break   #这里也可以令 judge = False
    else:
        print("输入有误，请重新输入！")