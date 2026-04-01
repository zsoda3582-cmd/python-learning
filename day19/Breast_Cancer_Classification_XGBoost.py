# ======================
# 1️⃣ 数据加载
# ======================
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
#读数据、划分x,y
data = load_breast_cancer()
x = pd.DataFrame(data.data,columns = data.feature_names)
y = data.target

#划分训练集、测试集
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=0
)

# ======================
# 2️⃣ 模型训练
# ======================
model = XGBClassifier(
    n_estimators = 100,
    max_depth =3,
    learning_rate = 0.1,
    random_state = 100
)
model.fit(x_train,y_train)
print("训练集准确率(random_state=100):",model.score(x_train,y_train))
print("测试集准确率(random_state=100):",model.score(x_test,y_test))

# from sklearn.metrics import confusion_matrix,precision_score,recall_score,accuracy_score
# y_pred = model.predict(x_test)
#
# y_prob = model.predict_proba(x_test)
# y_prob = model.predict_proba(x_test)[:,1]
#
# print("confusion_matrix:\n",confusion_matrix(y_test,y_pred))
# print("accuracy_score:",accuracy_score(y_test,y_pred))
# print("precision_score:",precision_score(y_test,y_pred))
# print("recall_score:",recall_score(y_test,y_pred))
#
# from sklearn.metrics import precision_score, recall_score, accuracy_score, confusion_matrix
#
# # 先拿到预测为1的概率
# y_prob = model.predict_proba(x_test)[:, 1]
#
# # 不同 threshold
# y_pred_03 = (y_prob > 0.3).astype(int)
# y_pred_05 = (y_prob > 0.5).astype(int)
# y_pred_07 = (y_prob > 0.7).astype(int)
#
# print("===== threshold = 0.3 =====")
# print("confusion_matrix:\n", confusion_matrix(y_test, y_pred_03))
# print("accuracy:", accuracy_score(y_test, y_pred_03))
# print("precision:", precision_score(y_test, y_pred_03))
# print("recall:", recall_score(y_test, y_pred_03))
#
# print("\n===== threshold = 0.5 =====")
# print("confusion_matrix:\n", confusion_matrix(y_test, y_pred_05))
# print("accuracy:", accuracy_score(y_test, y_pred_05))
# print("precision:", precision_score(y_test, y_pred_05))
# print("recall:", recall_score(y_test, y_pred_05))
#
# print("\n===== threshold = 0.7 =====")
# print("confusion_matrix:\n", confusion_matrix(y_test, y_pred_07))
# print("accuracy:", accuracy_score(y_test, y_pred_07))
# print("precision:", precision_score(y_test, y_pred_07))
# print("recall:", recall_score(y_test, y_pred_07))


# ======================
# 3️⃣ threshold选择（重点）
# ======================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score,recall_score
y_prob = model.predict_proba(x_test)[:,1]
thresholds = np.arange(0.0,1.0,0.05)
best_t = 0
target_recall = 0.95
best_precision = -1
for t in thresholds:
    y_pred = (y_prob>t).astype(int)
    p = precision_score(y_test, y_pred)
    r = recall_score(y_test,y_pred)
    if r >= target_recall:
        if p > best_precision:
            best_precision = p
            best_t = t
print("满足 recall >= 0.95 时，最佳 threshold:",best_t)
print("对应 precision:", best_precision)

# ======================
# 4️⃣ 最终评估（重点）
# ======================
y_pred_best = (y_prob > best_t).astype(int) #这一步是将选定的threshold应用于模型中来预测概率，将其结果转换为（0/1），再用其来进行模型整体评估
from sklearn.metrics import confusion_matrix,precision_score,recall_score,accuracy_score
print("confusion_matrix:\n",confusion_matrix(y_test,y_pred_best))
print("precision_score:",precision_score(y_test,y_pred_best))
print("recall_score:",recall_score(y_test,y_pred_best))
print("accuracy_score:",accuracy_score(y_test,y_pred_best))


plt.figure()
plt.plot(thresholds,precisions,label="precisions")
plt.plot(thresholds,recalls,label="recalls")
plt.xlabel("Thresholds")
plt.ylabel("Scores")
plt.title("Precision & Recall vs Threshold")

plt.legend()
plt.show()

"""
# Breast Cancer Classification (XGBoost)

## 1. Project Goal
这个项目是在做分类问题，也就是是否患癌，实现预测是否患癌，同时重点优化recall（减少漏诊）

## 2. Model
用的XGBoost模型（性能较强的集成学习方法）

## 3. Evaluation Metrics
precision:被预测为癌症的样本中，实际为患癌的概率
recall：在真实癌症中，被预测为癌症的比例
confusion_matrix
accruracy:模型准确率
我发现我还是讲不清楚这四个参数

## 4. Threshold Tuning
因为在模型中应用不同的Threshold，模型评估指标值不同，我们按情景来进行调节,通过调整threshold实现不同指标之间的权衡。

## 5. Final Result
最终recall达到98%以上，precision也达到95%以上，在医疗场景中，为了避免漏诊（false negative），优先保证较高的recall。

## 6. Key Insight
最重要的是学到了不同指标的使用，不同场景要分开讨论，比如本场景预测患癌一定不能“漏人”，所以高recall非常重要，而不是单独追求高accuracy；其次了解了几个指标
"""