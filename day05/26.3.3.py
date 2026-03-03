"""
my_str = "tonight we will go to dinner together"

value1 = my_str[9]
value2 = my_str[-28]
print(f"从字符串中取下标为9的字符:{value1},从字符串中取下标为-28的字符:{value2}")

value3 = my_str.index("will")
print(f"字符串will在字符串中的起始下标为：{value3}")

my_str_rep = my_str.replace("dinner","lunch")
print(f"把字符串{my_str}中的dinner替换成了lunch:{my_str_rep}")

list = my_str.split("e")
print(list)
print(my_str)
my_str1 = " etonight we will go to dinner together "
my_str11 = my_str1.strip()
my_str12 = my_str11.strip("er")
print(f"去除掉{my_str1}前后的空格后：{my_str11}")
print(f"去除掉{my_str11}前后的er后：{my_str12}")

cnt = my_str.count("e")
print(f"在字符串{my_str}中，出现e的次数是：{cnt}")

length = len(my_str)
print(f"字符串{my_str}的长度是：{length}")

练习题1:分割字符串
给定一个字符串:"itheima itcast boxuegu"
统计字符串内有多少个"it"字符。
将字符串内的空格，全部替换为字符:"|"
并按照|"进行字符串分割，得到列表

字符串itheima itcast boxuegu中有:2个it字符
字符串itheima itcast boxuegu，被替换空格后，结果:itheima|itcast|boxuegu
字符串itheimalitcastlboxuegu，按照|分隔后，得到:['itheima','itcast','boxuegu']

str = "itheima itcast boxuegu"
cnt = str.count("it")
print(f"字符串{str}中有：{cnt}个it字符")
str1 = str.replace(" ","|")
print(f"字符串{str}，被替换空格后，结果：{str1}")
str2 = str1.split("|")
print(f"字符串{str1}，按照|分隔后，得到{str2}")

练习题2：字符串清洗
用户输入一句带空格的字符串，如：
"  hello   world   "
要求：
	• 去掉前后空格
	• 把连续空格变成一个空格
	• 输出 "hello world"
提示：
用 strip() 和 " ".join(s.split()) 组合即可。

str = "  hello   world  dddd "
str1 = str.strip(" ")
print(str1)
str2 = " ".join(str1.split())
print(str2)


练习题3：敏感词替换
输入一句话：
请输入内容：你真笨蛋
将敏感词 "笨蛋" 替换成 "**"。
输出：
你真**

print("输入一句话：")
str = input()
str1 = str.replace("笨蛋","**")
print(str1)

"""
# #自定义一个字典
# my_dict = {"zy":100,"dgq":99,"zyz":101}
#
# #定义空字典（2种）
#
#
# #打印字典内容及类型
# my_dict["zt"] = 100
# my_dict["dgq"] = 96
# k = my_dict.pop("zt")
# print(my_dict)
# print(k)
# my_dict.clear()
# print(my_dict)

# keys = my_dict.keys()
# print(keys)
# for key in keys:
#     print(f"字典的key是：{key}")
#     print(f"字典的value是：{my_dict[key]}")
#
# for key in my_dict:
#     print(f"字典的key是：{key}")
#     print(f"字典的value是：{my_dict[key]}")
#
# cnt = len(my_dict)
# print(cnt)

#
# info_dict = {
#     "wlh":{
#         "dept":"tech",
#         "sala":3000,
#         "level":1
#     },
#     "zjl":{
#         "dept":"mark",
#         "sala":5000,
#         "level":2
#     },
#     "ljl":{
#         "dept":"mark",
#         "sala":7000,
#         "level":3
#     },
#     "zxy":{
#         "dept":"tech",
#         "sala":4000,
#         "level":1
#     }
# }
# for name in info_dict:
#     if info_dict[name]["level"] == 1:
#         info_dict[name]["level"] = info_dict[name]["level"] + 1
#         info_dict[name]["sala"] = info_dict[name]["sala"] + 1000
# print(f"全体员工级别为1的员工完成升职加薪操作，操作后：")
# print(info_dict)

# 练习题4：成绩字典练习
# 创建一个字典：
# scores = {"小明": 88, "小红": 92, "小刚": 76}
# 实现：
# 	• 添加一个学生成绩
# 	• 修改某个学生分数
# 	• 删除某个学生
# 输出所有学生和成绩

# score = {
#     "小明":88,
#     "小红":92,
#     "小刚":76
# }
# score["悦悦"] = 100
# score["小明"] = 99
# score.pop("小刚")
# print(score)

# 练习题5：小项目（15–20 分钟）——“单词统计器”
# 用户输入一段英文文本：
# 例如：
# hello world hello python
# 输出每个单词出现了几次：
# hello: 2
# world: 1
# python: 1
# 知识点：
# 	• split
# 	• 循环
# 	• 字典计数

sentence = input()
count = {}
list = sentence.split(" ")
print(list)
for item in list:
    count[item] = count.get(item, 0) + 1
print(count)
count[item] = count.get(item,0) +1