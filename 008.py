#第八个练习 - 逢七拍腿游戏

#游戏规则：几个人围圈坐一起，从1开始数数，当数到尾数是7或者7的倍数时，不报出该数，拍一下腿。
#请问从1数到99，假设每个人都没有出错，一共要拍多少次腿

count = 0
for num in range(1,100):
    if num%7 == 0 or num%10 == 7:
        count += 1
print("从1数到99，一共要拍" + str(count) + "多少次腿。")


#还可以改为
'''
count = 0
for num in range(1,100):
    str_num = str(num)
    if num%7 == 0 or str_num.endswith('7'):
        count += 1
print("从1数到99，一共要拍" + str(count) + "多少次腿。")
'''

#或者还可以改为（书本上的解法）
'''
total = 99
for number in range(1,100):
    if number%7 == 0:
        continue
    else:
        string = str(number)
        if string.endswith('7'):
            continue
    total -= 1
print("从1数到99，一共要拍" + str(total) + "多少次腿。")
'''