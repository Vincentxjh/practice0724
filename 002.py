#第二个练习 - 输出玫瑰花语

#引言
print("在古希腊神话中，玫瑰集爱情和美丽于一身，所以人们常用玫瑰来表示爱情。")
print("但是不同朵数的玫瑰代表的含义不同。")

#获取用户输入的朵数，转换为整形
number = int(input("请输入您想送几朵玫瑰花，我会告诉您含义："))

#根据不同朵数，分别输入不用含义
if number == 1:
    print("1朵：你是我的唯一！")
elif number == 3:
    print("3朵：I Love You！")
elif number == 10:
    print("10朵：十全十美！")
elif number == 99:
    print("99朵：天长地久！")
elif number == 108:
    print("108朵：求婚！")
else:
    print("我也不知道了！试试送1朵、3朵、10朵、99朵或108朵。")