#第十二个练习 - 模拟10086查询功能

print("----------10086查询功能----------\n")
print("输入1：查询当前余额\n"
    "输入2：查询当前剩余流量\n"
    "输入3：查询当前剩余通话\n"
    "输入0：退出自助查询系统\n")
judge = True
while judge:
    num = input()
    if num == "1":
        print("当前余额为：999元")
    elif num == "2":
        print("当前剩余流量为：5G")
    elif num == "3":
        print("当前剩余通话为：189分钟")
    elif num == "0":
        print("退出自助查询系统！")
        judge = False   #这里也可以用break
    else:
        print("输入有误，请重新输入！")