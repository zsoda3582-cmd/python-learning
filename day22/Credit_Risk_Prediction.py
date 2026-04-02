import pandas as pd
df = pd.read_csv("loan_data.csv")
df.info()
print("--------------------------------------------------------------------")
print(df.head(10))
print("--------------------------------------------------------------------")
print(df.shape)
print("--------------------------------------------------------------------")
print(df.columns)

# 拆 X 和 y
x = df.drop("loan_status",axis=1)
y = df["loan_status"]

# 类别编码
x = pd.get_dummies(x,drop_first = True)

# 划分数据
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42,stratify=y
)

# 建模
from xgboost import XGBClassifier
model = XGBClassifier(
    eval_metric = "logloss",
    random_state=42
)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
y_prob = model.predict_proba(x_test)[:,1]

from sklearn.metrics import accuracy_score,recall_score,precision_score,confusion_matrix
print("confusion_matrix:\n",confusion_matrix(y_test,y_pred))
print("accuracy_score:",accuracy_score(y_test,y_pred))
print("recall_score:",recall_score(y_test,y_pred))
print("precision_score:",precision_score(y_test,y_pred))
print("--------------------------------------------------------------------")

y_pred_03 = (y_prob > 0.3).astype(int)
print("confusion_matrix_0.3:\n",confusion_matrix(y_test,y_pred_03))
print("accuracy_score_0.3:",accuracy_score(y_test,y_pred_03))
print("recall_score_0.3:",recall_score(y_test,y_pred_03))
print("precision_score_0.3:",precision_score(y_test,y_pred_03))
print("--------------------------------------------------------------------")

y_pred_07 = (y_prob > 0.7).astype(int)
print("confusion_matrix_0.7:\n",confusion_matrix(y_test,y_pred_07))
print("accuracy_score_0.7:",accuracy_score(y_test,y_pred_07))
print("recall_score_0.7:",recall_score(y_test,y_pred_07))
print("precision_score_0.7:",precision_score(y_test,y_pred_07))
print("--------------------------------------------------------------------")

y_pred_08 = (y_prob > 0.8).astype(int)
print("confusion_matrix_0.8:\n",confusion_matrix(y_test,y_pred_08))
print("accuracy_score_0.8:",accuracy_score(y_test,y_pred_08))
print("recall_score_0.8:",recall_score(y_test,y_pred_08))
print("precision_score_0.8:",precision_score(y_test,y_pred_08))
print("--------------------------------------------------------------------")

#可视化
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import recall_score,precision_score

thresholds = np.linspace(0,0.99,50) #在0-1之间，均匀地取50个数，用来批量测试thresholds
precision_list = []
recall_list = []

for t in thresholds:
    y_pred_t = (y_prob > t).astype(int)
    recall = recall_score(y_test,y_pred_t)
    precision = precision_score(y_test,y_pred_t)

    recall_list.append(recall)
    precision_list.append(precision)

plt.figure()
plt.plot(thresholds,recall_list,label="recall")
plt.plot(thresholds,precision_list,label="Precision")
plt.xlabel("Thresholds")
plt.ylabel("Score")
plt.title("Precision & Recall vs Thresholds")
plt.legend() #显示标签
plt.grid()   #显示网格线，更方便看
plt.show()
print("--------------------------------------------------------------------")

import numpy as np
recall_arr = np.array(recall_list)
precision_arr = np.array(precision_list) #把python列表转化成numpy数组
f1 = 2 * (recall_arr * precision_arr)/ (recall_arr + precision_arr) #f1 score（调和平均）:同时考虑 precision 和 recall 的综合分数
best_idx = np.argmax(f1)
best_t = thresholds[best_idx]

# 输出：
# 最优 threshold
# 对应的 precision
# 对应的 recall
print("best_threshold",best_t)
print("best_precision",precision_arr[best_idx])
print("best_recall",recall_arr[best_idx])
