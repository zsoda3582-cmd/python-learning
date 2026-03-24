# Python Learning Log

## Day01
- 基础输入输出
- BMI 计算
- 小练习

## Day02
- if 判断
- while 循环
- for 循环
- 猜数字游戏
- 99 乘法表
- 发工资案例

## Day03
- 函数定义与调用
- 函数参数与返回值
- 全局变量与局部变量
- ATM 银行操作系统（存取款、查询）
- 猜数字游戏（函数版）

## Day04 
- 列表基础
- 列表操作
- 购物车程序
- To-Do小项目

## Day05
- 字符串基础
- 字符串常用方法（strip / split / replace / find）
- 字典基础（增删改查）
- 小项目：单词统计器

## Day06
- 文件读写
- try-except 基础
- 迷你记账本项目

## Day07
- NumPy 基础
- ndarray 创建与 shape
- 索引与切片
- 数组运算与统计函数
- 学生成绩数组分析练习
- 分析销售数据练习

## Day08 Titanic 数据分析day1

今天完成：
1. 使用 pandas 读取 Titanic 数据
2. 查看数据结构（shape / columns / head）
3. 统计男女数量
4. 计算不同性别生存率
5. 计算不同舱位生存率
6. 使用 matplotlib 画柱状图

发现：
- 女性生存率约 74%
- 男性生存率约 19%
- 头等舱生存率最高

问题：
为什么女性生存率更高？
（Women and children first）

期待明天的分析学习！

## Day09 Titanic 数据分析day2

- 分析了性别与生存率的关系
- 分析了舱位与生存率的关系
- 分析了年龄组与生存率的关系
- 分析了票价组与生存率的关系，并绘制了散点图

第一个小项目完成！
学到了：
- read_csv
- head / shape / columns
- value_counts
- groupby + mean
- pd.cut
- plot(kind="bar")
- hist()
- scatter()
现在还不够顺手，这很正常，因为熟练不是靠“听懂”，而是靠“再做 1~2 个类似项目”，
继续加油！

## Day10 Student Scores 数据分析项目（分两天完成的）

- 使用 pandas 读取学生成绩数据
- 查看数据结构 (shape / columns / head)
- 计算各科平均分 (mean)
- 按性别分组分析成绩 (groupby + mean)
- 使用 matplotlib 绘制可视化图表
- 柱状图（性别 vs 平均成绩）
- 直方图（数学成绩分布）
- 散点图（数学 vs 英语成绩关系）

进一步扩展分析：
- 极值分析
- 找到各科最高分和最低分 (max / min)
- 创建新列 Total（总成绩）
- 找到总成绩最高的学生 (idxmax + loc)
- 分析总成绩分布（直方图）
- 分析科目之间关系（散点图）
- Math vs Python
- English vs Python
- 使用 describe() 查看完整统计信息

巩固 & 学到了了函数的使用：
- max()
- min()
- describe()
- 创建新列 df["Total"]
- idxmax()
- loc
- matplotlib 可视化练习

项目总结：
通过 Student Scores 数据分析项目，进一步熟悉了 pandas 和 matplotlib 的核心用法，包括：

- 数据读取与结构查看
- 分组统计
- 极值分析
- 创建新列
- 数据可视化
- 使用 idxmax + loc 查询特定数据

这个项目让我更加熟悉数据分析的基本流程：
读取数据 → 数据探索 → 统计分析 → 可视化 → 得出结论。


## Day11 Netflix 数据分析 day1

今天完成：
- 使用 pandas 读取 Netflix 数据
- 查看数据结构（shape / columns / head）
- 使用 describe() 查看数据统计信息
- 统计 Movie / TV Show 数量（value_counts()）
- 使用柱状图展示不同类型影视作品数量
- 分析 Netflix 各年份发布作品数量趋势
- 使用折线图可视化内容增长趋势
- 使用 str.contains() 搜索标题关键词
- 分析 Netflix 内容来源国家
- 使用 split() + explode() 统计前 10 国家并绘制柱状图

学到：
- value_counts()
- str.contains()
- str.split()
- explode()
- plot(kind="bar")
- 折线图趋势分析

## Day12 Netflix 数据分析 day2

今天完成：
- 分析 Netflix 内容分级（rating）分布
- 使用 value_counts() 统计不同 rating 数量
- 发现 rating 列中存在异常值（如 "74 min"）
- 清洗异常数据，保留正常 rating 数据
- 将 rating 合并为三类：Kids / Teen / Adult
- 使用 apply() 创建新列 Rating_Group
- 统计 Kids / Teen / Adult 三类内容数量并绘制柱状图
- 分析不同内容类型（Kids / Teen / Adult）随年份变化趋势
- 使用 groupby() + size() + unstack() 整理数据并绘制折线图

学到：
- 数据清洗
- apply()
- 自定义分类函数
- groupby()
- size()
- unstack()
- 分类统计与趋势分析

小结：
- Netflix 平台以 Adult 内容为主，其次是 Teen，Kids 较少
- rating 数据中存在异常值，分析前需要先清洗
- 不同内容类型可以通过分组和折线图观察年份变化趋势

## Day13 Titanic ML 项目 day1

今天完成：
- 复习 pandas 基础操作（shape / head / 列选择）
- 使用 pandas 读取 Titanic 数据
- 划分 X / y
- 使用 train_test_split 划分数据集
- 使用 model.fit 训练模型
- 使用 model.predict 进行预测

学到：
- 机器学习基本流程（数据 → 训练 → 预测）
- fit：学习规律
- predict：做预测
- 预测只用 X，不用 y

小结：
- 跑通 Titanic 基础 ML 流程
- 还未进行数据处理和模型评估


## Day14 Titanic ML 项目 day2-3 
# 模型结论：
- 加了 FamilySize 特征
- 发现特征工程能提升模型效果
- 没有random控制，模型结果存在波动
- 加入 Fare 特征后模型效果提升
- 随机森林在当前特征下表现优于逻辑回归
- 交叉验证结果约为 0.79，说明模型性能稳定
  
# 学到的核心点
- 特征工程对模型影响很大
- 单次结果不可靠，需要交叉验证
- 不同模型在不同特征下表现不同
