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


## Day15 Housing Price Prediction (California Housing)

数据分析（EDA）
- 数据无缺失值
- 所有特征为数值型
- 相关性分析显示：
  - MedInc 与房价相关性最高

模型对比
1️⃣ 线性回归（Linear Regression）
- MSE ≈ 0.556
特点：
- 简单
- 可解释性强
- 但无法处理复杂非线性关系
---
2️⃣ 随机森林（Random Forest）
- MSE ≈ 0.255
特点：
- 能捕捉非线性关系
- 明显优于线性模型
---
简单调参
| 模型 | MSE |
|------|-----|
| RandomForest (50 trees) | ~0.257 |
| RandomForest (100 trees) | ~0.255 |

结论：
- 树数量增加带来小幅提升
- 存在性能与速度的权衡
---
特征重要性分析
Top features：
- MedInc（最重要）
- AveOccup
- Latitude / Longitude
说明：收入和地理位置对房价影响最大

---
项目总结
- 房价预测问题具有明显非线性特征
- 随机森林模型显著优于线性回归
- 模型选择比简单调参更重要

## Day16 House_Price_Advanced_project_day01
今天完成：
* 使用 pandas 读取 Kaggle 房价数据（train / test）
* 使用 seaborn 绘制 `SalePrice` 分布图
* 发现房价数据呈右偏分布，对 `SalePrice` 进行 `log` 变换，使分布更接近正态
* 统计各特征缺失值情况（按缺失数量排序）
* 处理缺失值：
  * 类别型特征：填充 `"None"`（表示没有该属性）
  * 数值型特征：使用 `median` 填充
* 使用 `pd.get_dummies()` 进行特征编码（类别 → 数值）
* 数据维度变化：
  * 原始特征：81
  * 编码后特征：631
* 划分训练集 / 测试集（train_test_split）
* 训练模型：
  * Ridge 回归
  * Lasso 回归（调参 alpha=0.001）

小结：
* 跑通了房价预测完整流程（EDA → 数据处理 → 建模）
* 初步理解了正则化模型（Ridge / Lasso）
* Lasso 从 631 个特征中筛选出约 91 个有效特征
* 模型效果已有明显提升

## Day17 House_Price_Advanced_project_day02
继续完善模型与优化：
- Lasso 调参（alpha）：尝试不同 alpha 值（0.1 → 0.0001）。观察模型分数变化，发现：
    alpha 过大 → 约束过强 → 欠拟合 → 分数下降
    alpha 过小 → 约束过弱 → 可能过拟合
    存在一个最优区间（本实验约在 0.003 左右）
- 模型理解加深
    alpha 控制特征筛选强度
    Lasso 可以自动进行特征筛选（使部分特征系数变为 0）
- 特征工程：新增特征：TotalSF = GrLivArea + TotalBsmtSF（房屋总面积）
                    HouseAge = YrSold - YearBuilt（房龄）
  目的：构造更有意义的特征，提高模型表达能力
- 数据标准化：使用 StandardScaler
    让不同特征处于相同尺度，避免某些特征影响过大，对 Lasso 收敛和效果有明显提升
- 收敛问题优化
    调整 max_iter（迭代次数）
    解决 Lasso 的收敛警告（Objective did not converge）

小结
- 理解了 Lasso 中 alpha 的作用（不是越小越好，而是存在最优值）
- 掌握了基本调参思路（固定数据 → 改参数 → 看结果）
- 初步理解特征工程的重要性（可以显著影响模型表现）
- 标准化 + 调参 可以明显提升模型稳定性和效果

## Day18 House_Price_Advanced_project_day03 项目优化+收尾
- 项目目标（用已有条件预测房价）
- 做了哪些处理[1.log(因为大部分房屋价格都在低中价位，少量房价很高，就会导致房价分布直方图右边拖尾，log就是应对“右偏分布场景的”)；2.缺失值(数据集中缺失值分为非数值型、数值型，非数值型填None，数值型填0或者中位数median，不用mean是因为极值会把平均值拉偏)3.特征工程(基于我们的现实理解，人为地基于现有条件重新造一些新条件，更好地协助模型训练)；4.标准化(像房屋年份这种特征有1900、2000的，但有些二分类特征值只有0、1，不同特征尺度差太大，会影响正则化的效果，标准化是为了让正则化更公平。)]
- 用了什么模型（Ridge模型做的是L2正则化，会降低模型特征的系数，但不会直接置为0；Lasso会把某些特征系数直接置为0来做特征筛选）
- 调参结论（alpha越大，模型对特征约束越强；alpha越小约束越弱。经实验，验证了本环境下alpha ≈ 0.003 最好）
- 学到的最重要三点（1.数据处理是更重要的，而模型训练只占很小一部分，大部分精力都在处理数据，这是我新学到的很重要甚至颠覆我对机器学习的认知的知识！2.标准化很重要，但这个知识点不像我对alpha这种直白的、很显示就能看出差别的参数理解的这么全面，后面还希望继续练习；3.别放弃，永远记住一点：I can handle it!）

## Day19+20 Breast_Cancer_Classification_XGBoost 项目

- 项目目标:本项目是一个二分类问题，基于乳腺癌数据集，预测患者是否患癌。在本项目中，不仅关注模型整体准确率（accuracy），更重要的是：在医疗场景下，尽量减少漏诊（false negative），因此优先优化 recall。
- 使用模型

- 使用模型：XGBoost（集成学习方法，性能较强）
    - 训练方式：train_test_split 划分训练集 / 测试集
    - 主要参数：n_estimators、max_depth = 3、learning_rate = 0.1
- 评估指标（重点理解）
    - **precision（精确率）**  
      被预测为“患癌”的样本中，实际为患癌的比例  👉 关注：是否乱报
    - **recall（召回率）**  
      所有真实患癌样本中，被正确预测出来的比例  👉 关注：是否漏诊（最重要）
    - **accuracy（准确率）**  
      所有预测中，预测正确的比例  👉 但在本任务中不是最关键指标
    - **confusion_matrix（混淆矩阵）**  
      用于分析 TP / FP / FN / TN 的具体情况

- Threshold 调整（核心部分）:默认模型使用 threshold = 0.5，但在实际任务中,不同 threshold 会影响 precision 和 recall 的平衡

- 本项目通过：1.遍历多个 threshold（0 ~ 1）;2.在 **recall ≥ 0.95** 的前提下;3.选择 **precision 最大** 的 threshold ,用以上3步来确定最合适的分类阈值
- 调整 threshold 后，模型表现为：recall ≈ 98%+ precision ≈ 95%+  accuracy ≈ 96%+

👉 说明模型能够：几乎不漏诊（recall高）、同时误报也控制在合理范围（precision不低）


- 项目总结

通过本项目，我完成了：

- 基础分类模型训练（XGBoost）
- precision / recall / accuracy 的理解与应用
- confusion matrix 的分析
- threshold 调整与模型行为控制
- 从“跑模型”到“根据任务目标优化模型”的转变

## Day21+22 Telco_Customer_Churn_XGBoost 项目

- 项目目标
* 预测用户是否流失（Churn）
* 在模型基础上理解 **precision / recall / threshold 的关系**

- 项目总结
* 学会处理真实数据问题（隐藏缺失值）：TotalCharges 是字符串（含空格）——处理方式：1. 空字符串 → None 2.再 转换为 float 3.删除缺失值；删除无用特征：customerID（避免无意义编码）
* 掌握类别特征编码:使用 `pd.get_dummies()` 进行 One-Hot 编码, `drop_first=True`：去掉重复信息（避免多重共线性）， 最终特征数：约 30 个
* 理解 precision / recall 的权衡关系： threshold ↓ → recall ↑（少漏人），threshold ↓ → precision ↓（多误判）， 本质是：模型决策标准的调整
* 能通过 threshold 主动控制模型行为
