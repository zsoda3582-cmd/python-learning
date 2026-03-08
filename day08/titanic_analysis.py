import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("titanic.csv")
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
print(f"不同性别的生存率为：{df.groupby("Sex")["Survived"].mean()}")
print(f"不同舱位的生存率为：{df.groupby("Pclass")["Survived"].mean()}")

print(df.groupby("Pclass")["Survived"].mean().plot(kind = "bar"))
plt.show()

print(df.groupby("Sex")["Survived"].mean().plot(kind = "bar"))
plt.show()
