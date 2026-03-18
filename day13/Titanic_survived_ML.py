# 读取数据
# 读取数据："Survived", "Pclass", "Sex", "Age"
#删除缺失行
#打印前5行
import pandas as pd
df = pd.read_csv("titanic.csv")
df = df[["Survived","Pclass","Sex","Age"]]
df = df.dropna()
print(df.head())
print("----------------------------------------------------------------------")
print(df["Sex"])

#特征编码（encoding）
df["Sex"] = df["Sex"].map({"female" : 1,"male" : 0})
print(df["Sex"])
print("----------------------------------------------------------------------")

#拆分x和y
x = df[["Pclass","Sex","Age"]]
y = df["Survived"]

#划分训练集 / 测试集
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.2,random_state = 42
)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
print(f"准确率为：{accuracy_score(y_test,y_pred)}")