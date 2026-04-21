from unicodedata import numeric
import pandas as pd
df = pd.read_csv("telco.csv")
print(df.head())
print("------------------------------------")
df.info()
print("------------------------------------")
print(df.columns)
print("------------------------------------")

#特征TotalCharges数值转换处理
print(df["TotalCharges"].dtype)
print((df["TotalCharges"] == " ").sum())
print("------------------------------------")
df["TotalCharges"] = df["TotalCharges"].replace(" ",pd.NA)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])
print(df["TotalCharges"].dtype)
#特征TotalCharges缺失值处理
print(df["TotalCharges"].isnull().sum())
#总共7043行，11行缺失，建议直接删掉；其他缺失值处理方法：均值填充、0填充
df = df.dropna(subset=["TotalCharges"]) #只检查TotalCharges这一列，有缺失值就删此列
print(df["TotalCharges"].isnull().sum())
print(df.shape)

#目前为止的逻辑链：发现问题 → 定位列 → 检查异常 → 转换类型 → 处理缺失
print("------------------------------------")

print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True))
print("------------------------------------")
print(pd.crosstab(df["Contract"],df["Churn"],normalize="index"))
print("------------------------------------")
print(pd.crosstab(df["InternetService"],df["Churn"],normalize="index"))
print("------------------------------------")
print(pd.crosstab([df["InternetService"],df["Contract"]],df["Churn"],normalize="index"))
"""
结论1：月付（Month-to-month）用户流失率最高，说明“没有长期绑定”的用户最不稳定。
结论2：光纤（Fiber optic）用户流失率高于DSL，说明高消费用户更容易流失。
结论3：“光纤 + 月付”用户流失率最高（约54.6%），是最核心的高风险人群。本质上，这群人“高价值 + 高要求 + 低忠诚”
"""
print("------------------------------------")

#先按 Churn 分组(“流失”一组，“不流失”一组)，再在每组里取 MonthlyCharges，两组分别求平均值
print(df.groupby("Churn")["MonthlyCharges"].mean())
print(df.groupby("Churn")["tenure"].mean())
"""
结论4：流失用户的平均月费用更高（74.44元 vs 61.30元），说明高费用用户更容易流失。
结论5：流失用户的平均使用时长更短（17.98月 vs 37.65月），说明新用户更容易流失。
"""
print("------------------------------------")
print(df.groupby("Contract")["tenure"].mean())

print("------------------------------------")
#处理数据
df["Churn"] = df["Churn"].map({"No":0,"Yes":1})
df = df.drop("customerID",axis = 1)
df = pd.get_dummies(df,drop_first = True)

#划分x,y
x = df.drop("Churn",axis = 1)
y = df["Churn"]

#划分数据集
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
    x,y,
    test_size = 0.2,
    random_state = 42,
    stratify = y
)

#建模 + 预测
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

#评估
from sklearn.metrics import accuracy_score,precision_score,recall_score
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Precision:",precision_score(y_test,y_pred))
print("Recall:",recall_score(y_test,y_pred))
"""
初步结论：
1.Accuracy = 0.804：模型整体预测对了大约 80.4%
2.Precision = 0.648：在模型预测为“会流失”的用户里，大约 64.8% 真的会流失，说明预测出的高风险用户有较好的可信度
3.Recall = 0.575：在所有真正会流失的用户里，模型找出来了大约 57.5%，说明模型仍会漏掉一部分真实流失用户。
因此，该模型可以作为客户流失预测的 baseline，但后续仍有优化空间。
"""