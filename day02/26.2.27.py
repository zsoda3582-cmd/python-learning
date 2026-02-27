"""
#1.猜数字
num = 29
if int(input()) == num:
    print("猜对啦真聪明！")
else:
    print("不对，再猜一次")
    if(int(input()) == num):
        print("猜对啦真聪明！")
    else:
        print("不对，再猜最后一次")
        if (int(input()) == num):
            print("猜对啦真聪明！")
        else:
            print("Sorry,全部猜错啦，我心里的是：29")

#2.猜数字题2：
要求：
1.数字随机产生，范围1-10
2.有3次机会猜测数字，通过3层嵌套判断实现
3.每次猜不中，会提示大了或小了

import random
num = random.randint(1,10)
x = int(input())
if x == num:
    print("Wow，真棒！一次就猜中了！")
else:
    if x > num:
        print("大了！")
    else:
        print("小了！")
    print("请重新输入：")
    y = int(input())
    if y == num:
        print("Wow，真棒！您猜中了！")
    else:
        if y > num:
            print("大了！")
        else:
            print("小了！")
        print("请重新输入：")
        z = int(input())
        if z == num:
            print("Wow，真棒！您终于猜中了！")
        else:
            print("不好意思~您的机会用完了，正确的数字是：",num)


#3.通过while循环，计算从1累加到100的和
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i = i + 1
print(sum)

#4.while循环猜数字题
import random
num = random.randint(1,100)
x=int(input())
while x!= num:
    if  x > num:
        print("大了")
    else:
        print("小了")
    x = int(input())
print("您终于猜对啦")

#5.实现print不换行
print("hello",end = ' ')
print("world")

#6.打印99乘法表
i = 1
while i < 10:
    j=1
    while j <= i:
        print(f"{j}*{i}={j*i:2d}",end=" ")
        j=j+1
    print("\n")
    i=i+1


#7.for循环练习题：数一数有几个a
name = "ithema is a brand of itcast"
cnt = 0
for i in name:
    if i == "a":
        cnt += 1
print(cnt)

"""
#8.for循环打印99乘法表
for i in range(1,10):
    j=1
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i:2d}",end=" ")
    print("\n")

"""
#9.练习案例：发工资
某公司，账户余额有1W元，给20名员工发工资。员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
如果工资发完了，结束发工资。
test
员工12，绩效分3，低于5，不发工资，下一位。
员工13，绩效分1，低于5，不发工资，下一位。
员工14，绩效分4，低于5，不发工资，下一位。
向员工15发放工资1000元，账户余额还剩余2000元
向员工16发放工资1000元，账户余额还剩余1000元
员工17，绩效分2，低于5，不发工资，下一位。
向员工18发放工资1000元，账户余额还剩余0元
工资发完了，下个月领取吧。
提示：
使用循环对员工依次发放工资
continue用于跳过员工，break直接结束发工资
import random
随机数可以用：
num = random.randint(1,10)

import random
money = 10000
for i in range(1,21):
    if money == 0:
        print("工资发完了，下个月领取吧。")
        break
    else:
        score = random.randint(1,10)
        if score < 5:
            print("员工",i,",绩效分",score,",低于5，不发工资，下一位。")
            continue
        else:
            money = money - 1000
            print("向员工",i,"发放工资1000元，账户余额还剩",money,"元")
"""