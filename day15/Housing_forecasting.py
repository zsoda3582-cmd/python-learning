import pandas as pd
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing() #数据包housing
df = pd.DataFrame(housing.data,columns=housing.feature_names) #创建表格
df["Price"] = housing.target
print(df.head())
print("------------------------------------------------------------------------------------")

print(df.info())
print("------------------------------------------------------------------------------------")

print(df.describe())
print("------------------------------------------------------------------------------------")

print(df.corr()["Price"].sort_values(ascending=False))
print("------------------------------------------------------------------------------------")

#先划分x和y
x = df.drop(["Price"],axis = 1)
y = df["Price"]

#划分训练集测试集
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size = 0.2,random_state = 42
)

#创建模型
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train) #训练
y_pred = model.predict(x_test) #测试

from sklearn.metrics import mean_squared_error
print(f"MSE：{mean_squared_error(y_test,y_pred)}") #评估

#x_train,x_test,y_train,y_test,y_pred
#首先训练当然用两者的训练集 model.fit(x_train,y_train)
#其次是测试，会生成一个新预测集"y_pred" 用x_test生成
#最后评估准确率/误差，用刚生成的预测集 和 实际y的真实值集合 y_test之间的差距来衡量
print("------------------------------------------------------------------------------------")

print(model.coef_)
print(model.intercept_)
print("------------------------------------------------------------------------------------")

#拿一条真实数据用模型预测
row = x_test.loc[[0]]
print(row)
print(f"模型计算结果：{model.predict(row)}")

#手动模拟模型计算
import numpy as np
manual_pred = np.dot(model.coef_,row.values[0]) + model.intercept_
print(f"手动计算结果：{manual_pred}")
print("----------------------------------------------")

#开始标准化训练
#导包
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#创建标准化工具
scaler = StandardScaler()
#用训练集学习标准
x_train_scaled = scaler.fit_transform(x_train)
#用同样的标准处理测试集
x_test_scaled = scaler.transform(x_test)

#创建模型
model2 = LinearRegression()
#训练
model2.fit(x_train_scaled,y_train)
#预测
y_pred2 = model2.predict(x_test_scaled)
#评估
mse2 = mean_squared_error(y_pred2,y_test)
print("标准化后的MSE:",mse2)
print("----------------------------------------------")

#随机树模型
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
rf_model = RandomForestRegressor(random_state = 42)
rf_model.fit(x_train,y_train)
y_pred_rf = rf_model.predict(x_test)
mse3 = mean_squared_error(y_test,y_pred_rf)
print(f"随机生成树的MSE为：{mse3}")
print("----------------------------------------------")

#比较不同树的数量之下的模型误差
# #建树
# rf_model_50 = RandomForestRegressor(n_estimators = 50,random_state = 42)
# rf_model_100 = RandomForestRegressor(n_estimators = 100,random_state = 42)
#
# #训练
# rf_model_50.fit(x_train,y_train)
# rf_model_100.fit(x_train,y_train)
#
# #测试
# y_pred_rf_50 = rf_model_50.predict(x_test)
# y_pred_rf_100 = rf_model_100.predict(x_test)
#
# #评估
# mse_rf_50 = mean_squared_error(y_test,y_pred_rf_50)
# mse_rf_100 = mean_squared_error(y_test,y_pred_rf_100)
# print(f"50棵树的MSE：{mse_rf_50}\n100棵树的MSE：{mse_rf_100}")
# print("----------------------------------------------")
#

#随机树看特征重要性
import pandas as pd
feature_importance = pd.DataFrame({
    "Feature":x.columns,
    "Importance":rf_model.feature_importances_
})
#排序
feature_importance = feature_importance.sort_values(by="Importance",ascending=False)
print(feature_importance)




