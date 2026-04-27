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

## Day21 Telco_Customer_Churn_XGBoost 项目

- 项目目标
1.预测用户是否流失（Churn）
2.在模型基础上理解 **precision / recall / threshold 的关系**

- 项目总结
1.学会处理真实数据问题（隐藏缺失值）：TotalCharges 是字符串（含空格）——处理方式：1. 空字符串 → None 2.再 转换为 float 3.删除缺失值；删除无用特征：customerID（避免无意义编码）
2.掌握类别特征编码:使用 `pd.get_dummies()` 进行 One-Hot 编码, `drop_first=True`：去掉重复信息（避免多重共线性）， 最终特征数：约 30 个
3.理解 precision / recall 的权衡关系： threshold ↓ → recall ↑（少漏人），threshold ↓ → precision ↓（多误判）， 本质是：模型决策标准的调整
4.能通过 threshold 主动控制模型行为

好，这次我给你写一个**干净、精简、像你之前风格的 README**，你可以直接复制用👇

---
## Day22 Credit_Risk_Prediction（信用风险预测）
---
# 项目目标
* 预测贷款用户是否违约（loan_status）
* 理解模型在不同特征变化下的决策行为
* 在 precision / recall 之间找到合适的平衡点

---
# 数据处理
* 删除目标列：`loan_status`
* 类别特征：`pd.get_dummies()` 编码
* 划分数据集：`train_test_split(test_size=0.2, stratify=y)`
---

# 模型
* 使用模型：XGBoost
* 输出：违约概率（`predict_proba`）

# 评价指标：
* accuracy
* precision
* recall
* confusion matrix
---

# Threshold 调整
* 通过 `predict_proba` 获取预测概率
* 手动测试多个 threshold（0.3 / 0.7 / 0.8 等）
* 观察 precision 与 recall 的变化

👉 结论：
* threshold ↓ → recall ↑，precision ↓
* threshold ↑ → precision ↑，recall ↓
---

# 可视化分析
* 绘制 Precision / Recall 随 threshold 变化曲线
* 观察两者的 trade-off（权衡关系）
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/e3e4e592-3f66-406f-8975-a5298c5c3821" />

---
# 最优 threshold（F1）
* 使用 F1 score（precision + recall 的平衡）选择最佳 threshold
```
threshold ≈ 0.46  
precision ≈ 0.88  
recall ≈ 0.83  
```
---

## What-if 分析（模型行为分析）
👉 思路：固定一个客户，只改变单个特征，观察模型预测变化

# 收入（person_income）分析
* 改变收入，同时同步调整 `loan_percent_income`
* 观察违约概率变化
👉 结论：
* 收入较高时 → 风险较低
* 收入下降时 → 风险逐步上升
* 当收入较低且贷款占比高时 → 风险急剧上升
* 模型反应不是完全平滑（树模型的分段特性）
# 实验图
<img width="753" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/2aa132f1-e4ee-4b66-a561-2c1ace8787d7" />
---
# 核心结论
* `loan_percent_income`（贷款占收入比例）是关键风险因素
* 极端输入会导致模型输出剧烈变化
* XGBoost（树模型）对特征变化的响应是非线性的
* 模型解释（what-if 分析）比单纯准确率更重要

---
## Day22 Credit_Risk_Prediction（信用风险预测）收尾
# 信用分（credit_score）分析
* 固定 base_customer，仅改变信用分
* 观察违约概率变化
---

# 实验结果
* 信用分较低（500）→ 风险较高（≈0.13）
* 信用分从 500 → 550 → 风险显著下降
* 信用分 ≥ 700 → 风险接近 0，变化趋于稳定
<img width="800" height="500" alt="Figure_3" src="https://github.com/user-attachments/assets/3e2c7b85-7d53-42d6-8223-b88400ca23e9" />

---
# 现象总结
* 风险随信用分提升整体下降
* 在低信用分区间存在明显“跳变”
* 高信用分区间进入“稳定区”

---
# 原因分析
* 树模型基于阈值划分 → 导致分段变化
* 模型对低信用分样本更敏感
* 一旦达到安全区间，模型不再区分细微差异

## Day24-1 Telco Churn Prediction（客户流失预测）
# 项目目标：预测客户是否会流失（Churn = Yes / No）

---
# 数据预处理
 核心点：
* TotalCharges 原本是字符串（有空格）
* 删除缺失值（只有 11 条，影响很小）
* get_dummies 进行独热编码

---
# 探索性分析（EDA）

* 合同类型 vs 流失率
月付（Month-to-month）流失率最高
一年 / 两年合同用户更稳定
👉 结论：没有长期绑定的用户更容易流失

---
* 网络类型 vs 流失率
光纤（Fiber optic）用户流失率最高
DSL 次之
无网络服务用户最低
👉 结论：高消费用户更容易流失

---
* 组合分析（网络 + 合同）
“光纤 + 月付” 流失率最高（≈ 54.6%）
👉 结论：高价值 + 无绑定用户 = 高风险人群

---
# 数值特征分析

```python
df.groupby("Churn")["MonthlyCharges"].mean()
df.groupby("Churn")["tenure"].mean()
```
结果：
* 流失用户：
  * 月费用更高（74.44 vs 61.30）
  * 使用时间更短（17.98 vs 37.65）
👉 结论：新用户 + 高费用用户更容易流失

---
# 建模（Logistic Regression）
模型评估结果
| 指标        | 数值    |
| --------- | ----- |
| Accuracy  | 0.804 |
| Precision | 0.648 |
| Recall    | 0.575 |

---
# 模型分析
* Accuracy 较高（≈80%），说明整体预测效果不错
* Precision = 64.8%，说明预测为“流失”的用户中，大部分确实会流失
* Recall = 57.5%，说明仍有一部分流失用户未被识别

👉 结论：模型具备一定预测能力，但对流失用户的识别仍有提升空间

---
# 总结

* 客户流失与以下因素显著相关：
  * 合同类型（是否月付）
  * 网络类型（是否光纤）
  * 月费用
  * 使用时长

* 高风险用户画像：光纤 + 月付 + 高费用 + 新用户

* 当前模型为 baseline，可进一步优化：
  * 标准化特征
  * 尝试 XGBoost / RandomForest
  * 调整阈值优化 Recall

---
# 🌱 项目收获

* 熟练掌握：

  * 数据清洗流程
  * EDA 分析思路
  * 分类模型基本流程
* 理解：
  * Precision / Recall 的业务含义
  * 特征与业务之间的联系
---
## Day24-2：Telco Customer Churn Prediction v1 收尾————模型优化（Threshold Tuning）

# 问题背景

在 baseline 模型中：
* Accuracy ≈ 0.80
* Precision ≈ 0.65
* Recall ≈ 0.57

📌 问题：模型会漏掉较多真实流失用户（Recall 偏低）
---

# 优化思路

不直接使用默认 threshold=0.5，而是：
👉 遍历不同 threshold
👉 计算 Precision / Recall / F1
👉 找到 F1-score 最大的 threshold

---
# 关键代码
```python
thresholds = np.linspace(0,1,50)

for t in thresholds:
    y_pred_new = (y_prob > t).astype(int)
```

# 最优结果
* Best threshold ≈ 0.41
* Best F1 ≈ 0.63
---

# 优化效果
| 指标        | baseline | 优化后        |
| --------- | -------- | ---------- |
| Recall    | 0.57     | **0.68 ↑** |
| Precision | 0.65     | 0.58 ↓     |
---

# 结论
📌 降低 threshold 后：
* 能抓住更多流失用户（Recall 提升）
* 但误判有所增加（Precision 下降）
👉 属于典型的 **Precision-Recall trade-off**

---
# 最终模型策略
选择较低 threshold（≈0.41）：
👉 更适合“流失预警”场景
👉 优先减少漏掉高风险用户

---
# 项目总结
本项目完成了：
* 数据清洗（TotalCharges）
* EDA分析（用户行为特征）
* Logistic 回归建模
* 阈值优化（业务导向决策）

📌 核心提升：
* 理解 Recall / Precision 的业务意义
* 掌握 threshold 调整方法
* 能基于业务目标优化模型

---
## 🔍 模型对比分析（Logistic vs XGBoost）
在本项目中，对比了线性模型（Logistic Regression）与树模型（XGBoost）在客户流失预测任务中的表现。

# 1️⃣ Logistic Regression
- 作为 baseline 模型
- 优点：结构简单、可解释性强
- 表现：Precision 较高，但 Recall 偏低
- 特点：偏保守，容易漏掉流失用户

# 2️⃣ XGBoost
- 作为升级模型
- 优点：能够捕捉非线性关系与特征组合
- 表现：Recall 提升，Precision 略有下降
- 特点：更偏激进，抓取流失用户能力更强

# 综合结论
在 churn 预测场景中，更关注 Recall（减少漏判），因此 XGBoost 更适合作为实际应用模型。
同时，通过 threshold tuning，可以进一步在 Precision 和 Recall 之间进行权衡，实现业务目标优化。

## Day 25+26 NLP_Text_Classification and Compare —— IMDB 文本情感分类（模型对比）
# 本项目基于 IMDB 影评数据集，完成文本情感分类任务（正面 / 负面），并对比了不同机器学习模型在同一任务下的表现差异。
# 数据集:
- 数据来源：IMDB Dataset（本地 CSV）
- 数据规模：50,000 条影评
- 标签：positive → 1（正面） && negative → 0（负面）
# 方法流程
- 整体 pipeline:文本 → TF-IDF 向量化 → 模型训练 → 分类预测
- 文本向量化（TF-IDF）作用：1.将文本转换为数值特征  2.降低高频无意义词（如 the / and）的影响  3.强化具有区分能力的词（如 amazing / terrible
# 模型对比
① Logistic Regression（逻辑回归）
- 每个词对应一个权重（coef）
- 能较好利用 TF-IDF 特征
- 对文本分类任务表现稳定
② Multinomial Naive Bayes（朴素贝叶斯）
- 基于词频概率进行分类
- 假设词之间相互独立
- 计算简单，训练速度快
# 实验结果
| 模型                  | Accuracy | 特点        |
| ------------------- | -------- | --------- |
| Logistic Regression | 0.90     | 表现稳定，整体更优 |
| Naive Bayes         | 0.89     | 速度快，但略有偏差(正分类上的recall较低) |
- 原因分析（关键理解）：Naive Bayes 的核心假设——词之间相互独立，但在真实语言中not good ≠ good，模型无法理解“词之间的组合关系”，导致在复杂表达（如否定句）中容易误判。
# 模型理解（进阶）
通过分析 LogisticRegression 的 coef 发现模型已学到情感特征：
- 正权重词：great / excellent / amazing
- 负权重词：bad / worst / terrible
同时也发现：it / and 等词也可能出现权重，是因为模型学习的是“统计相关性”，而非语义理解
# 项目收获
通过本项目，我完成了：
- 从结构化数据 → NLP 的过渡
- 理解 TF-IDF 的作用
- 掌握文本分类基本 pipeline
- 能够分析不同模型的表现差异
# 总结：
Logistic Regression 在文本分类任务中表现更稳定，
而 Naive Bayes 虽然简单高效，但由于独立性假设，
在复杂语言结构中表现受限。
