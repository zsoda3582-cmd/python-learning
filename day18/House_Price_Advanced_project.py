import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#1.读数据+处理目标变量（解决右偏分布）
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
train.head()
sns.histplot(train["SalePrice"])
plt.show()
train["SalePrice"] = np.log1p(train["SalePrice"])
sns.histplot(train["SalePrice"])
plt.show()

#2.合并数据
train["is_train"] = 1
test["is_train"] = 0
test["SalePrice"] = 0
all_data = pd.concat([train,test],axis = 0)

#3.数据预处理
    #处理缺失值
missing = train.isnull().sum()
missing = missing[missing > 0].sort_values(ascending = False)
print(missing.head(10))
print("----------------------------------------------------------------")

all_data["PoolQC"] = all_data["PoolQC"].fillna("None")
all_data["Alley"] = all_data["Alley"].fillna("None")
all_data["Fence"] = all_data["Fence"].fillna("None")
all_data["FireplaceQu"] = all_data["FireplaceQu"].fillna("None")
all_data["GarageType"] = all_data["GarageType"].fillna("None")
all_data["GarageQual"] = all_data["GarageQual"].fillna("None")
all_data["GarageFinish"] = all_data["GarageFinish"].fillna("None")
all_data["GarageCond"] = all_data["GarageCond"].fillna("None")
all_data["BsmtFinType2"] = all_data["BsmtFinType2"].fillna("None")
all_data["BsmtExposure"] = all_data["BsmtExposure"].fillna("None")
all_data["BsmtQual"] = all_data["BsmtQual"].fillna("None")
all_data["BsmtCond"] = all_data["BsmtCond"].fillna("None")
all_data["BsmtFinType1"] = all_data["BsmtFinType1"].fillna("None")
all_data["MiscFeature"] = all_data["MiscFeature"].fillna("None")
all_data["MasVnrType"] = all_data["MasVnrType"].fillna("None")

all_data["MasVnrArea"] = all_data["MasVnrArea"].fillna(0) #MasVnrArea 是数值列，给它填 "None" 字符串，会把这一列搞成混合类型,通常填 0 比较自然

all_data["LotFrontage"] = all_data["LotFrontage"].fillna(all_data["LotFrontage"].median())
all_data["GarageYrBlt"] = all_data["GarageYrBlt"].fillna(all_data["GarageYrBlt"].median())


    #特征工程
all_data["TotalBath"] = (
    all_data["FullBath"] + 0.5 * all_data["HalfBath"]
    +all_data["BsmtFullBath"] + 0.5 * all_data["BsmtHalfBath"]
)
all_data["isRemodeled"] = (
    all_data["YearRemodAdd"] != all_data["YearBuilt"]
).astype(int)
all_data["TotalSF"] = all_data["GrLivArea"] + all_data["TotalBsmtSF"]

    #get_dummies操作
all_data = pd.get_dummies(all_data)

#4.拆回训练集
train_data = all_data[all_data["is_train"]==1]
test_data = all_data[all_data["is_train"]==0]
x = train_data.drop(["SalePrice","is_train"],axis = 1)
y = train_data["SalePrice"]

#5.建模、训练模型
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
    #划分训练集/测试集
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size = 0.2
)
    #标准化
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

    #训练、打分
model = Lasso(alpha=0.003,max_iter = 20000)
model.fit(x_train_scaled,y_train)
print(f"标准化后的lasso模型打分(alpha = 0.003）：{model.score(x_test_scaled, y_test)}")
#模拟一次考试，流程：划分训练集、测试集 ->用训练集讯息 ->用测试集打分
#普通评估：一次考试，只考一次，运气好分就高，运气差分就低



from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
model = make_pipeline(
    StandardScaler(),
    Lasso(alpha=0.003,max_iter=20000)
)
scores = cross_val_score(model,x,y,cv=5,scoring="r2")
print("5折交叉验证R2:",scores)
print("平均R2:",scores.mean())
#交叉验证，考5次，再取平均：数据分5份（cv=5），每一份轮流当测试集，共训练5次
#不靠运气，更稳定、真实

model.fit(x, y)
coef = model.named_steps["lasso"].coef_
print("Lasso保留特征数：",np.sum(coef!=0))
print("总特征数：",len(coef))
#正式训练一个”最终模型“，上面cross+val_score的模型不会留下来，需要一个”真正学完的模型“


"""
1. 这个项目在干嘛？
这个项目在用各种条件来建模，比如房子面积、是否有篱笆地下室面积等条件，建模目的是预测房价

2. 数据长什么样？
有的是文字，后面要通过get_dummies操作来将这些文字转化成数字（PS:get_dummies还有拆列的作用）

3. 我做了哪些处理？（重点,每一步只写“为什么”）
处理数据缺失值，对于非数字型的，用None补充；数字型的用中位数median补充（不用mean是因为mean可能会被极值带偏）

4. 我用了什么模型？
Ridge和Lasso模型（各有什么特点忘了）
Ridge：防止过拟合，让模型更稳定。主要让系数变小、提升稳定性，但通常不会把系数直接压成 0。
Lasso：除了防过拟合，还可以把不重要的特征变成0（做特征筛选）

5. 我发现了什么？
Lasso模型分数更高，alpha值越高，约束越强，会将更多的特征系数变为0，值为1时“砍掉”太多，模型信息不足，训练的很差很差
标准化后的lasso模型打分(alpha = 0.1）：   0.7081945576014919
标准化后的lasso模型打分(alpha = 0.01）：  0.9064577630479129
标准化后的lasso模型打分(alpha = 0.005）： 0.9162237960900771
标准化后的lasso模型打分(alpha = 0.003）： 0.9171419783232536 ！！！！！！
标准化后的lasso模型打分(alpha = 0.002）： 0.9167629215056001
标准化后的lasso模型打分(alpha = 0.001）： 0.9150799220160026
标准化后的lasso模型打分(alpha = 0.0005）：0.9111070470463865
标准化后的lasso模型打分(alpha = 0.0001）：0.9020555354422013
我试了不同的alpha，发现并不是alpha越小，约束越强就越好的，而是有一个分界值，本实验中分界值为0.003，或许再细化会更好

6. 我做了哪些优化？
新加了两列分别是房子总面积和房龄，这步应该叫特征工程吧，反正就是根据我们自己的理解，造出可能利于模型训练的“条件”；
做标准化，让值步差距太大（讲不清楚）
用max_iter控制迭代轮次，这个第一次见



读数据、log处理右偏
all_data
数据处理（处理缺失/特征工程/get_dummies）
拆回数据
训练模型
"""

