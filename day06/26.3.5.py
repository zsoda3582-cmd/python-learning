"""
演示对文件的读取
"""

#打开文件
f = open("D:/测试.txt","r",encoding = "utf-8")
# print(type(f))

#读取文件
# print(f.read())
# line1 = f.readlines()
# line2 = f.readlines()
# print(line1)
# print(line2)

#for循环读取文件行
# for line in f:
#     print(line)

#with open语法操作文件：
# with open("D:/测试.txt","r",encoding = "utf-8") as f:
#     for line in f:
#         print(line)

"""
演示捕获异常
"""
#基本捕获语法
try:
    f = open("D:/test.txt","r",encoding = "utf-8")
except:
    f = open("D:/test.txt","w",encoding = "utf-8")

# 练习 1：文件写入日志
# 用户输入一句话，将内容写入 log.txt 文件中。
# 要求：用户每输入一次，就追加一行。

# while True:
#     print("1 添加记录")
#     print("2 查看记录")
#     print("q 退出")
#     choice = input("请选择：")
#     if choice == "1":
#         print("请输入记录全称：")
#         line = input()
#         f = open("D:/log.txt", "w", encoding="utf-8")
#         f.write(line)
#     elif choice == "2":
#         f = open("D:/log.txt", "r", encoding="utf-8")
#         for i in f:
#             print(f"{i}\n")
#     else:
#         break
#
# 练习1：
#
# while True:
#     print("1 添加记录")
#     print("2 查看记录")
#     print("q 退出")
#
#     choice = input("请选择：")
#
#     if choice == "1":
#         line = input("请输入记录内容：")
#         f = open("D:/log.txt","a",encoding = "utf-8")
#         f.write(line + "\n")
#         f.close()
#     elif choice == "2":
#         f = open("D:/log.txt","r",encoding = "utf-8")
#         for i in f:
#             print(i)
#         f.close()
#     else:
#         break


# 练习 2：读取文件内容
# 读取 log.txt 并按行输出：
# 1. xxx
# 2. yyy
# 3. zzz
# （索引 + 内容结合）

# i=1
# with open("D:/log.txt","r",encoding = "utf-8") as f:
#     for line in f:
#         print(f"{i}.{line}")
#         i = i + 1
#
#
# 练习 3：异常处理练习
# 写一个读取文件的程序：
# 	• 如果文件不存在 → 提示：“文件不存在，请检查路径”
# 	• 程序不会崩溃
#
# try:
#     f = open("D:/ttwxhyt.txt","r",encoding = "utf-8")
# except:
#     print("文件不存在，请检查路径")

# 练习4：综合项目——“迷你记账本系统”
# 功能：
# 	1. 添加一条记账记录（收入 or 支出 + 金额 + 备注）
# 	2. 所有记录写入 records.txt
# 	3. 查看历史记录
# 	4. 程序不因用户输错而崩（用 try-except）
# 示例：
# 请选择：1
# 类型（收入/支出）：收入
# 金额：200
# 备注：工资
# 记录已保存！
# 请选择：2
# --- 历史记录 ---
# 收入 200 工资
# 支出 30 午餐

print("功能\n1.添加一条记账记录（收入or支出）\n2.查看历史记录")
while True:
    print("请选择：")
    choice = input()
    if choice == "1":
        print("请输入类型（收入/支出）：")
        ty = input()
        print("请输入金额：")
        money = input()
        print("请输入备注：")
        memo = input()
        f = open("D:/records.txt","a",encoding = "utf-8")
        f.write(f"{ty},{money},{memo}\n")
        print("记录已保存！")
        f.close()
    elif choice == "2":
        f = open("D:/records.txt","r",encoding = "utf-8")
        for line in f:
            print(line,end="")
        f.close()
    else:
        print("您的输入有问题，请重新输入！")
