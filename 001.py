#第一个练习 - 判断输入的是不是黄蓉所说的数

#一个数除三余二，除五余三，除七余二，判断这是数是几
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？")
number = int(input("请输入你认为满足条件的数："))
if number%3 == 2 and number%5 == 3 and number%7 == 2:
    print(str(number) + " 这个数符合条件：三三数之剩二，五五数之剩三，七七数之剩二。")
else:
    print("这个数不符合条件！")