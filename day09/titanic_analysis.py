import pandas as pd
import matplotlib.pyplot as plt
# from pandas.conftest import observed

# =====================
# 读取数据
# =====================
df = pd.read_csv("titanic.csv")
# =====================
# 数据基本信息
# =====================
print(df.shape)
print("----------------------------")
print(df.columns)
print("----------------------------")
print(df.head())
print("----------------------------")
print(df["Sex"].value_counts())
print("----------------------------")
print(df.groupby("Sex")["Survived"].count())
print("----------------------------")

#看不同性别、舱位的生存率
# =====================
# 性别 vs 生存率
# =====================
print(f"不同性别的生存率为：{df.groupby("Sex")["Survived"].mean()}")
# =====================
# 舱位 vs 生存率
# =====================
print(f"不同舱位的生存率为：{df.groupby("Pclass")["Survived"].mean()}")

print(df.groupby("Pclass")["Survived"].mean().plot(kind = "bar"))
# plt.show()

print(df.groupby("Sex")["Survived"].mean().plot(kind = "bar"))
# plt.show()

# =====================
# 年龄数据
# =====================
print("年龄数据描述")
print(df["Age"].describe())

# =====================
# 按年龄分组
# =====================
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins = [0,12,18,35,60,80],
    labels = ["child","teen","young","adult","old"]
)
print(df["AgeGroup"].value_counts())

print("不同年龄组生存率：")
print(df.groupby("AgeGroup",observed = True)["Survived"].mean())

print("票价vs生存率")
print(df["Fare"].describe())
df.hist()
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

# =====================
# 按票价分组
# =====================
df["FareGroup"] = pd.cut(
    df["Fare"],
    bins = [0,20,50,100,600],
    labels = ["low","medium","high","very high"]
)
print("不同票价档位生存率：")
print("-------------------------------------------------------------------------------------------------")
print(df.groupby("FareGroup",observed = True)["Survived"].mean().plot(kind = "bar"))
plt.title("Survived rate by Fare Group")
plt.xlabel("Fare Group")
plt.ylabel("Survived rate")
plt.show()

# =====================
# 年龄 vs 票价 散点图
# =====================
# 关键一步：把 Age 或 Fare 为空的行删掉，不然绘图函数会“过敏”
clean_df = df.dropna(subset  = ["Age","Fare"])
plt.scatter(clean_df["Age"],clean_df["Fare"],alpha = 0.5) #alpha是透明度，散点重叠时看的更清楚
plt.title("Age vs Fare Distribution")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
# 结论：
# 票价与年龄没有明显关系，
# 票价主要由舱位决定。
df["Age"].hist()
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
