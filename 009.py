#第九个练习 - 模拟支付宝蚂蚁森林的能量产生过程

source = input("查询能量请输入能量来源！退出程序请输入0 \n"
               "能量来源如下：\n"
               "生活缴费、行走捐、共享单车、线下支付、网络购票 \n")
if source == "0":
    print("已退出！")
elif source =="生活缴费" or source =="行走捐" or source =="共享单车" or source =="线下支付" or source =="网络购票":
    print("200g")
else:
    print("输入有误，请重新输入！")