#第七个练习 - 打印久久乘法表

#利用双层for循环嵌套
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i) + "x" + str(j) + "=" + str(i * j), end=" ")
    print()

#为了使打印看起来工整，也可以使用以下打印方法
#print("%dx%d=%-3d" % (i, j, i * j), end=" ")
#print(str(i) + "x" + str(j) + "=" + str(i * j) + "\t", end=" ")