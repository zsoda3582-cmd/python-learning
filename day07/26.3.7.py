# import numpy as np
#
# a = np.array([
#     [1,2,3,4],
#     [34,22,453,262]]
# )
# print(a)
# print(a.shape)
# print(a[0,0])
#
# b = np.array(
#     [
#         [3,4,5,2],
#         [26,224,7,2]
#     ]
# )
# print(a * b)
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))
# print(np.sum(a))

#练习1：学生成绩数组分析练习
# 1. 创建一个二维数组
# 表示 3 个学生、4 门课成绩：
# [
#     [85, 90, 78, 92],[88, 76, 95, 80],[90, 91, 89, 87]
# ]
# 2. 打印这个数组的 shape

# 3. 取出：
# 第一个学生的所有成绩、第二门课的所有学生成绩
#
# 4. 计算：
# 所有成绩的平均值、每个学生的平均成绩、每门课的平均成绩、最高分、最低分

# 5. 给所有成绩加 5 分
# import numpy as np
# scores = np.array(
#     [
#         [67,89,66,77],
#         [88,89,68,89],
#         [78,90,80,83]
#     ]
# )
# print(scores.shape)
# print(scores[0])
# print(scores[:,1])
# print(f"所有成绩的平均值为：{scores.mean()}")
# print(f"每个学生的平均成绩是：{scores.mean(axis = 1)}")
# print(f"每门课的平均成绩为：{scores.mean(axis = 0)}")
# print(f"最高分为：{scores.max()}")
# print(f"最低分为：{scores.min()}")
# print(f"给所有成绩加5分之后的成绩为：{scores+ 5}")

#练习2：分析销售数据
# 假设有一个商店 4 天的销售额：
# sales = np.array([
#     [100, 120, 130],
#     [90, 110, 125],
#     [115, 140, 150],
#     [105, 130, 160]
# ])
# 含义：4 天 × 3 个商品
# 1 打印 shape
# 2 取出第一天所有商品销售额、商品B四天销售额
# 3 计算每一天总销售额、每个商品总销售额
# 4 找出销售额最高值、销售额最低值
# 5 假设所有销售额增加10%
import numpy as np
sales = np.array(
    [
        [100,120,130],
        [90,110,125],
        [115,140,150],
        [105,130,160]
    ]
) #4天*3个商品
print(sales.shape)
print(f"第一天所有商品销售额为：{sales[0]}，商品B4天销售额为：{sales[:,1]}")
print(f"每一天总销售额为：{sales.sum(axis = 1)}，每个商品总销售额为：{sales.sum(axis = 0)}")
print(f"销售额最高值为：{sales.max()},销售额最低值为：{sales.min()}")
print(f"所有销售额增加10%之后为：{sales + 0.1*sales}")
