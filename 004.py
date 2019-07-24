#第四个练习 - 用while循环查找黄蓉所说的那个数

print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？")

#从1开始查找，直到找到满足条件的第一个数值为止
number = 1
while number:
    if number%3 == 2 and number%5 == 3 and number%7 == 2:
        print("答曰：这个数就是" + str(number))
        break
    number += 1