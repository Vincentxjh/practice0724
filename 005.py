#第五个练习 - 用for循环查找黄蓉所说的那个数

print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？")

#查找1～1000之内满足条件的数
number = 1
print("答曰：满足条件的数有：", end="")
for number in range(1,1000):
    if number%3 == 2 and number%5 == 3 and number%7 == 2:
        print(number, end=" ")