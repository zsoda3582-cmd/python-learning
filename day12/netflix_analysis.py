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
print("---------------------------------------------------------")


# =====================
# 画柱状图
# =====================
top_country.plot(kind = "bar")
plt.title("the counts of movies in different countries")
plt.xlabel("different countries")
plt.ylabel("count")
# plt.show()

# =====================
# 先看一下 rating数量
# =====================
df_clean = df[~df["rating"].str.contains("min",na = False)].copy()
print(f"各种rating的数量：{df_clean["rating"].value_counts()}")
df_clean["rating"].value_counts().plot(kind = "bar")
plt.title("the counts of Rating")
plt.xlabel("the kinds of rating")
plt.ylabel("counts")
# plt.show()
print("---------------------------------------------------------")

# =====================
# 将rating 合并成三类
# =====================
def classify_rating(r):
    if r in["TV-Y","TV-Y7","TV-G","G"]:
        return "Kids"
    elif r in ["PG","PG-3","TV-PG","TV-14"]:
        return "Teen"
    else:
        return "Adult"

df_clean["Rating_Group"] = df_clean["rating"].apply(classify_rating)
df_clean["Rating_Group"].value_counts().plot(kind = "bar")
plt.title("the counts of different groups of Rating")
plt.xlabel("Rating_Group")
plt.xlabel("counts")
# plt.show()


# =====================
# Netflix 的内容类型，随时间是怎么变化的？即：Adult / Teen / Kids在不同年份的变化趋势
# =====================
year_group = df_clean.groupby(["release_year","Rating_Group"]).size()
year_group = year_group.unstack()

year_group.plot()
plt.title("content types over year")
plt.xlabel("release year")
plt.ylabel("count")
plt.show()

