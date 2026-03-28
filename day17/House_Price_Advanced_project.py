import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
train.head()
print("----------------------------------------------------------------")

sns.histplot(train["SalePrice"])
# plt.show()

train["SalePrice"] = np.log1p(train["SalePrice"])
sns.histplot(train["SalePrice"])
# plt.show()

#处理缺失值
missing = train.isnull().sum()
missing = missing[missing > 0].sort_values(ascending = False)
print(missing.head(10))
print("----------------------------------------------------------------")

train["PoolQC"] = train["PoolQC"].fillna("None")
train["Alley"] = train["Alley"].fillna("None")
train["Fence"] = train["Fence"].fillna("None")
train["FireplaceQu"] = train["FireplaceQu"].fillna("None")
train["GarageType"] = train["GarageType"].fillna("None")
train["GarageQual"] = train["GarageQual"].fillna("None")
train["GarageFinish"] = train["GarageFinish"].fillna("None")
train["GarageCond"] = train["GarageCond"].fillna("None")
train["BsmtFinType2"] = train["BsmtFinType2"].fillna("None")
train["BsmtExposure"] = train["BsmtExposure"].fillna("None")
train["BsmtQual"] = train["BsmtQual"].fillna("None")
train["BsmtCond"] = train["BsmtCond"].fillna("None")
train["BsmtFinType1"] = train["BsmtFinType1"].fillna("None")
train["MasVnrArea"] = train["MasVnrArea"].fillna("None")
train["MiscFeature"] = train["MiscFeature"].fillna("None")
train["MasVnrType"] = train["MasVnrType"].fillna("None")

train["LotFrontage"] = train["LotFrontage"].fillna(train["LotFrontage"].median())
train["GarageYrBlt"] = train["GarageYrBlt"].fillna(train["GarageYrBlt"].median())


missing = train.isnull().sum()
missing = missing[missing > 0].sort_values(ascending = False)
print(missing.head(10))
print("----------------------------------------------------------------")

print(train.shape)
train = pd.get_dummies(train)
print(train.shape)
print("----------------------------------------------------------------")


#开始建模！！！！
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
x = train.drop(["SalePrice"],axis = 1)
y = train["SalePrice"]
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size = 0.2
)
model = Ridge()
model.fit(x_train,y_train)
print(f"Ridge模型打分：{model.score(x_test, y_test)}")

#换模型
from sklearn.linear_model import Lasso
model1 = Lasso(alpha=0.001)
model1.fit(x_train,y_train)
print(f"Lasso模型打分：{model1.score(x_test, y_test)}")
print("----------------------------------------------------------------")

import numpy as np
coef = model1.coef_
selected_features = np.sum(coef!=0)
print(f"Lasso保留了{selected_features}个特征")
print("----------------------------------------------------------------")

#看看“最重要的特征是谁”
feature_names = x.columns
important_features = sorted(
    zip(feature_names,coef),
    key=lambda x:abs(x[1]),
    reverse = True
)
# print(important_features[:10])


#房子总面积=地上面积+地下室面积
train["TotalSF"] = train["GrLivArea"] + train["TotalBsmtSF"]
#卖房时的房龄
train["HouseAge"] = train["YrSold"] - train["YearBuilt"]

#重新get_dummies、划分xy、划分训练集、lasso模型训练
# train = pd.get_dummies(train) #不需重新分列操作了，因为新加的这两列本来就是数值列
x = train.drop("SalePrice",axis = 1)
y = train["SalePrice"]
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size = 0.2,random_state = 42
)

#标准化
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = Lasso(alpha = 0.0001,max_iter = 20000)
model.fit(x_train_scaled,y_train)
print(f"标准化后的lasso模型打分(alpha = 0.0001）：{model.score(x_test_scaled, y_test)}")

"""
1. 这个项目在干嘛？
这个项目在用各种条件来建模，比如房子面积、是否有篱笆地下室面积等条件，建模目的是预测房价

2. 数据长什么样？
有的是文字，后面要通过get_dummies操作来将这些文字转化成数字（PS:get_dummies还有拆列的作用）

3. 我做了哪些处理？（重点,每一步只写“为什么”）
处理数据缺失值，对于非数字型的，用None补充；数字型的用中位数median补充（不用mean是因为mean可能会被极值带偏）

4. 我用了什么模型？
Ridge和Lasso模型（各有什么特点忘了）
Ridge：防止过拟合，让模型更稳定 
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

"""

