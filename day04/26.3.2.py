# list = ["hello" , "my" , "name" , "is" , "zhanguyue"]
# print(list)
# print(type(list))
# print(list[1])


#列表各操作语法训练练习
# new_list = ['hhh',['zheshi','yige','liebiaozhongdeliebiao'],123,True]
# idx = new_list.index('hhh')
# print(idx)
# new_list[idx] = "buxuhhhle"
# print(new_list)
# new_list.insert(1,"shixixixi")
# print(new_list)
# new_list.append("over")
# print(new_list)
# ele = new_list.pop(1)
# print(new_list)
# print(ele)
# del new_list[1]
# print(new_list)
# new_list.remove(123)
# print(new_list)
# # new_list.clear()
# # print(new_list)
#
# list = [1,2,3,11,2,3,52,2,2]
# cnt = list.count(2)
# print(cnt)

#循环教学练习
# my_list = [1,2,55,2,33,7,4,624]
#
# def list_while_func():
#     """
#     使用while循环来遍历列表
#     :return: None
#     """
#     global my_list
#     index = 0
#     while index < len(my_list):
#         x = my_list[index]
#         print(x)
#         index += 1
#
# def list_for_func():
#     """
#     使用for循环来遍历列表
#     :return: None
#     """
#     for i in my_list:
#         print(i)
# list_for_func()
# print("----------")
# list_while_func()


#练习 1：学生成绩列表处理
# 写一个简单的程序：
# 	• 创建一个 scores = [88, 92, 79, 100, 67]
# 	• 求平均值
# 	• 输出最高分
# 	• 输出最低分
# 	• 自己加一个功能：把所有分数+5 看看效果
# 这相当于“列表 + 循环”结合，非常适合你现在这个阶段。
#
# scores = [88,92,79,100,67]
# sum = 0
# high = -99999
# low = 99999
# for i in scores:
#     sum = sum + i
#     if i> high:
#         high = i
#     if i < low:
#         low = i
# avg = sum/len(scores)
# index = 0
# while index <len(scores):
#     scores[index] = scores[index] + 5
#     index = index + 1
#
# print(f"The average score is {avg}")
# print(f"The highest score is {high}")
# print(f"The lowest score if {low}")
# for i in scores:
#     print(i)

# 练习 2：超市购物车小程序（你的手能写得很爽的那种）
# 要求：
# 	• 初始购物车为空列表：cart = []
# 	• 循环输入商品名（输入 q 退出）
# 	• 每加入一件，打印当前购物车内容
# 示例效果：
# 请输入商品：苹果
# 购物车：['苹果']
# 请输入商品：牛奶
# 购物车：['苹果', '牛奶']
# 这个练习非常适合喜欢“边做边验证”的你，会给你成就感。

# cart = []
# while True:
#     print("请输入商品：")
#     tem = input()
#     if tem != "q":
#         cart.append(tem)
#         print("购物车：",end = '')
#         print(cart)
#     else:
#         break

# 练习 3：简易待办事项 To-Do 列表系统”
# 功能：
# 	1. 显示菜单
# 	2. 添加任务
# 	3. 删除任务
# 	4. 查看所有任务
# 	5. 输入 q 退出
# 这是你写 ATM 的升级版，肯定能写，而且写起来会更开心。
# 示例流程：
# --- 待办系统 ---
# 1. 添加任务
# 2. 删除任务
# 3. 查看所有任务
# q. 退出
# 请选择：1
# 请输入任务：写作业
# 任务已添加！
# 请选择：3
# 所有任务：['写作业']
# 这个项目 Day4 能写完 100% 没问题！
# 做完你会非常有满足感。

print("--- 待办系统 ---\n1.添加任务\n2.删除任务\n3.查看所有任务\nq.退出\n")
tasks = []
while True:
    print("请选择：")
    tem = input()
    if tem != "q":
        if tem == "1":
            print("请输入任务：")
            task = input()
            tasks.append(task)
            print("任务已添加！")
        elif tem == "2":
            print("这是您目前的所有任务：")
            i = 0
            for task in tasks:
                print(f"任务{i+1}:{task}")
                i = i + 1
            print("请输入您要删除的任务：")
            task = input()
            if task in tasks:
                tasks.remove(task)
                print("任务已删除！")
            else:
                print("您输入的不是任务列表中包含的任务哦~")
        elif tem == "3":
            print("这是您目前的所有任务：")
            for index, task in enumerate(tasks):
                print(f"{index}:{task}")
    else:
        break

