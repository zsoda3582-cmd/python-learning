"""
print(666)
print(13.14)
print("哈哈哈up")
"""

money = 100
print("钱包还有：",money)
money -= 20
print("买了一杯红茶拿铁，钱包还有：",money,"元")

print(type(money))

string_type = type("开心的seconds女士")
int_type  = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)

second = str(11)
print("转换后的数字类型是：",type(second),"，",second)

num1 = 6
print("num1 / 2 = ",num1 / 2)
print("num1 // 2 = ",num1 // 2)
print("num1 % 2 = ",num1 % 2)
print("num1 ** 3 = ",num1 ** 3)

#任务1：
print("请输入你的姓名：")
name = input()
print(name,"你好！今天也是元气满满的一天呀~")

#任务2：
print("请输入两个数字：")
num11 = float(input())
num22 = float(input())

print("加：",num11 + num22)
print("减：",num11 - num22)
print("乘：",num11 * num22)
print("整除：",num11 / num22)

#任务3：
print("请输入您的身高（m）和体重（kg)")
height = float(input())
weight = float(input())
BMI = weight / (height ** 2)
print("您的BMI是：",BMI)
if BMI >= 18.5 and BMI < 25 :
    print("属于正常范围")
elif BMI >= 25 and BMI <30 :
    print("您超重了哦")
else:
    print("您的BMI属于肥胖范围，该减肥啦！")