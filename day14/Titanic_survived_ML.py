# 读取数据
# 读取数据："Survived", "Pclass", "Sex", "Age"
#删除缺失行
#打印前5行
import pandas as pd
df = pd.read_csv("titanic.csv")
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df = df[["Survived","Pclass","Sex","Age","FamilySize","Fare"]]
#df = df.dropna()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
#特征编码encoding
df["Sex"] = df["Sex"].map({"female":1,"male":0})

#拆分x和y
x = df[["Pclass","Sex","Age","FamilySize","Fare"]]
y = df["Survived"]

#划分训练集、测试集
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2
)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
print(f"逻辑回归模型准确率为：{accuracy_score(y_test,y_pred)}")

from sklearn.ensemble import RandomForestClassifier
model_rf = RandomForestClassifier()
model_rf.fit(x_train,y_train)
y_pred_rf = model_rf.predict(x_test)
print(f"随机森林模型准确率为：{accuracy_score(y_test,y_pred_rf)}")
print(f"特征重要性：{model_rf.feature_importances_}")


#交叉验证
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model,x,y,cv=5)
print(f"交叉验证结果：{scores}")
print(f"平均验证结果：{scores.mean()}")