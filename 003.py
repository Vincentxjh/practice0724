#第三个练习 - 判断是否为酒后驾车

print("为了您和他人的生命安全，严禁酒后驾驶车辆！")

#提示输入每100毫升血液的酒精含量
alcohol_content = float(input("请输入每100毫升血液的酒精含量（单位mg）："))

#判断含量是否超标
if alcohol_content < 20:
    print("您还不构成饮酒行为，可以开车，请注意安全！")
elif alcohol_content < 80:
    print("您已经达到酒后驾车的认定标准，请勿开车！")
else:
    print("您已经达到醉驾的认定标准，千万不能开车！")

#本例可以改为用if的嵌套格式，如下：
'''
if alcohol_content < 20:
    print("您还不构成饮酒行为，可以开车，请注意安全！")
else:
    if alcohol_content < 80:
        print("您已经达到酒后驾车的认定标准，请勿开车！")
    else:
        print("您已经达到醉驾的认定标准，千万不能开车！")
'''