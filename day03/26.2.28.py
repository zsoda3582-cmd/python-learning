"""
def my_len(data):
    cnt = 0
    for i in data:
        cnt += 1
    print((f"字符串{data}的长度是{cnt}"))
my_len("xinkuanluzekuan")

def add(x,y):
    print(f"{x}+{y}的结果是{x+y}")
add(153672.1877667136,71667272)

练习案例：升级版自动查核酸
定义一个函数，名称任意，并接受一个参数传入（数字类型，表示体温）
在函数内进行体温判断（正常范围：小于等于37.5度），并输出如下内容：
欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！
体温测量中，您的体温是：37.3度，体温正常请进！
欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！
体温测量中，您的体温是：39.3度，需要隔离！

def test_check(tempe):
    if tempe <= 37.5:
        print(f"欢迎来到星巴克！请出示您的健康码以及72小时核酸证明，并配合测量体温！\n在体温测量中，您的体温是{tempe}度，体温正常请进！")
    else:
        print(f"欢迎来到星巴克！请出示您的健康码以及72小时核酸证明，并配合测量体温！\n在体温测量中，您的体温是{tempe}度，需要隔离！")
test_check(36.8)
test_check(38.8)

def add(x,y):
    return x+y
result = add(153672.1877667136,71667272)
print(result)

def fun_b():
    print("---b---")
def fun_c():
    print("---c---")
def fun_a():
    print("---a---")
    fun_b()
    fun_c()
fun_a()


练习1、综合案例：
综合案例：黑马ATM
1/主菜单效果
---------主菜单----------
周杰轮，您好，欢迎来到黑马银行ATM。请选择操作：
查询余额[输入1]
存款   [输入2]
取款   [输入3]
退出   [输入4]
请输入您的选择：

2/查询余额效果
---------查询余额---------
周杰轮，您好，您的余额剩余：5000000元


3/存、取款效果
---------存款-----------
周杰轮，您好，您存款50000元成功
周杰轮，您好，您的余额剩余：5050000元
---------取款-----------
周杰轮，您好，您取款50000元成功
周杰轮，您好，您的余额剩余4950000元


money = 5000000

def check_money():
    print(f"---------查询余额---------\n周杰轮，您好，您的余额剩余：{money}元")
def in_money(num):
    global money
    money = money + num
    print(f"---------存款---------\n周杰轮，您好，您存款{num}元成功\n周杰轮，您好，您的余额剩余：{money}元")
def out_money(num):
    global money
    if money >= num:
        money = money - num
        print(f"---------取款---------\n周杰轮，您好，您取款{num}元成功\n周杰轮，您好，您的余额剩余：{money}元")
    else:
        print("很抱歉！您的余额不足！本次取款失败")


print("---------主菜单----------\n周杰伦，您好，欢迎来到黑马银行ATM。请选择操作：\n查询余额[输入1]\n存款   [输入2]\n取款   [输入3]\n退出   [输入4]\n请输入您的选择：")

while True:
    option_char = input()
    if option_char == "1":
        check_money()
    elif option_char == "2":
        num = int(input())
        in_money(num)
    elif option_char == "3":
        num = int(input())
        out_money(num)
    else:
        print("感谢您的本次光临！")
        break

练习2、四则运算
要求：
	• 写 add(a,b) / sub(a,b) / mul(a,b) / div(a,b)
	• div 要处理 b==0（返回 None 或打印提示都行，但别报错）
建议你这样测：
	• 让用户输入两个数
	• 调用四个函数输出结果

def add(a,b):
    return a+b
def sub(a,b):
    return  a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("被除数不能为0哦！")
        return None
    else:
        return a//b
a = int(input())
b = int(input())
res1 = add(a,b)
res2 = sub(a,b)
res3 = mul(a,b)
res4 = div(a,b)
print(f"{a}+{b}={res1}")
print(f"{a}-{b}={res2}")
print(f"{a}*{b}={res3}")
print(f"{a}//{b}={res4}")


练习3、加分练习
把 day02 的“猜数字”改成函数版（会让你对函数理解暴涨）：
	• gen_target()：生成随机数
	• get_guess()：读取用户输入并转 int（顺便做异常处理：输入不是数字就让他重输）
	• check_guess(guess, target)：返回 "大了/小了/对了"
	• play_game()：把整个流程串起来
"""
import random
def gen_target():
    return random.randint(1,100)
def check_guess(guess,target):
    if guess==target:
        print("对了！棒(๑•̀ㅂ•́)و✧")
        return True
    elif guess > target:
        print("大了！请继续输入：")
    else:
        print("小了！请继续输入：")
    return False
def play_game():
    target = gen_target()
    print("请输入您猜的数字：")
    guess = int(input())
    while not check_guess(guess,target):
        guess = int(input())

play_game()

# ===== 今日暂停点 =====
# 已完成：基本逻辑 + while循环 + 输入判断
# 明天要做：完善输入异常处理 && 上传git
