#读数据
import pandas as pd
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(f"shape",df.shape)
print(f"head(10)",df.head(10))
print(f"columns",df.columns)
print(f"info()")
df.info()
print("---------------------------------------------------------------------------------")
print(df["TotalCharges"].unique()[:20]) #unique()返回这一列所有不同的值；Python 的切片，格式为[start : end]，[:20]意思是从0取到19个，左闭右开
print(df["TotalCharges"].isna().sum())
print((df["TotalCharges"]==" ").sum())

print("---------------------------------------------------------------------------------")
#将空值替换成None，再将字符串转换成float类型，再删除空值
df["TotalCharges"] = df["TotalCharges"].replace(" ",None)
df["TotalCharges"] = df["TotalCharges"].astype(float)
df = df.dropna()
print(df["TotalCharges"].isna().sum())
df = df.drop(["customerID"],axis=1)

print("---------------------------------------------------------------------------------")
#特征编码
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
df.info()

print("---------------------------------------------------------------------------------")
df = pd.get_dummies(df,drop_first = True)
df.info()

print("---------------------------------------------------------------------------------")
#划分x，y，测试集，训练集
x = df.drop("Churn",axis=1)
y = df["Churn"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42,stratify=y #stratify：按类别比例来切数据
)
print(x.shape)
print(y.shape)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


print("---------------------------------------------------------------------------------")
#建模
from xgboost import XGBClassifier
model = XGBClassifier(
    use_label_encoder = False,
    eval_metric = "logloss",
    random_state=42
)
model.fit(x_train,y_train)
y_pred = model.predict(x_test,)
y_prob = model.predict_proba(x_test)[:,1]

from sklearn.metrics import confusion_matrix,precision_score,recall_score,accuracy_score
print("confusion_matrix:\n",confusion_matrix(y_test,y_pred))
print("precision_score:",precision_score(y_test,y_pred))
print("recall_score:",recall_score(y_test,y_pred))
print("accuracy_score:",accuracy_score(y_test,y_pred))

print("---------------------------------------------------------------------------------")
y_pred_03 = (y_prob > 0.3).astype(int)
print("precision_0.3",precision_score(y_test,y_pred_03))
print("recall_0.3",recall_score(y_test,y_pred_03))

y_pred_02 = (y_prob > 0.2).astype(int)
print("precision_0.2",precision_score(y_test,y_pred_02))
print("recall_0.2",recall_score(y_test,y_pred_02))

"""
通过降低threshold，从0.5到0.3再到0.2，模型recall从0.54提升至0.78，但precision从0.59降低至0.48，体现了典型的precision-recall trade-off。
在客户流失场景中，更高recall有助于减少潜在流失用户的遗漏
"""
