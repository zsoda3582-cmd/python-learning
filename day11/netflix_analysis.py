import pandas as pd
import matplotlib.pyplot as plt

# =====================
# 读取数据
# =====================
df = pd.read_csv("netflix_titles.csv")
print(f"数据形状：\n{df.shape}")
print("---------------------------------------------------------")

print(f"列名有：\n{df.columns}")
print("---------------------------------------------------------")

print(df.head())
print("---------------------------------------------------------")

print(df.describe())
print("---------------------------------------------------------")

# =====================
# 统计 Movie / TV Show 数量
# =====================
print(f"不同种类影片的数量\n{df["type"].value_counts()}")
df["type"].value_counts().plot(kind="bar")
plt.title("Figure 1.Different kinds of movies")
plt.xlabel("type")
plt.ylabel("count")
# plt.show()
print("---------------------------------------------------------")

# =====================
# 每年发布作品数量
# =====================
print(f"Netflix每年发布作品数量:\n{df["release_year"].value_counts().sort_index()}")
print(f"Netflix每年发布作品数量:\n{df["release_year"].value_counts().sort_index().plot(kind = "bar")}")
plt.title("Figure 2.Netflix Release by Year")
plt.xlabel("release_year")
plt.ylabel("count")
# plt.show()
print("---------------------------------------------------------")

# =====================
# 看看数据集里有没有这部剧
# =====================
print(df[df["title"].str.contains("Stranger", na=False)])
print("---------------------------------------------------------")

# =====================
# 看一眼 country 数据
# =====================
print(f"看一眼 country 数据:\n{df["country"].head(10)}")
print(f"直接统计：\n{df["country"].value_counts()}")
print("此处很多国家（中间被逗号隔开的）被当成一个国家了，所以不合理")


country_series = df["country"].dropna().str.split(", ").explode().str.strip()
top_country = country_series.value_counts().head(10)
print(top_country)

# =====================
# 画柱状图
# =====================
top_country.plot(kind = "bar")
plt.title("the counts of movies in different countries")
plt.xlabel("different countries")
plt.ylabel("count")
plt.show()

