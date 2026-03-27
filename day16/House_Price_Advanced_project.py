import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
train.head()
print("----------------------------------------------------------------")

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(train["SalePrice"])
# plt.show()

import numpy as np
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
print(important_features[:10])

