# =====================
# 创建分析脚本、读取数据
# =====================
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student_scores.csv")
print(f"数据的形状：{df.shape}")
print(f"列名：{df.columns}")
print(f"前五行：\n{df.head()}")
print("--------------------------------------------------------------------------------")

# =====================
# 基本统计:计算数学、英语、python平均分
# =====================
print(f"数学平均分为：{df["Math"].mean()}")
print(f"英语平均分为：{df["English"].mean()}")
print(f"python平均分为：{df["Python"].mean()}")
print("--------------------------------------------------------------------------------")

# =====================
# 按性别分组
# =====================
print(f"按性别分组后的各科平均分为：\n{df.groupby("Gender")[["Math", "English", "Python"]].mean()}")
print("--------------------------------------------------------------------------------")

# =====================
# 画柱状图
# =====================
df.groupby("Gender")[["Math","English","Python"]].mean().plot(kind = 'bar')
plt.title("Average scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Score")
plt.show()

# =====================
# 数学成绩分布图（直方图）
# =====================
df["Math"].hist()
plt.title("Histogram of Math")
plt.xlabel("Score")
plt.ylabel("Count")
plt.show()

# =====================
# 散点图（数学和英语两门课的关系）
# =====================
plt.scatter(df["Math"],df["English"],alpha = 0.5)
plt.title("Relationship between Math and English")
plt.xlabel("Math")
plt.ylabel("English")
plt.show()

# =====================
# 找最高分和最低分
# =====================
print(f"数学最高分：{df['Math'].max()}")
print(f"数学最低分：{df['Math'].min()}")
print(f"英语最高分：{df['English'].max()}")
print(f"英语最低分：{df['English'].min()}")
print(f"python最高分：{df['Python'].max()}")
print(f"python最低分：{df['Python'].min()}")
print("--------------------------------------------------------------------------------")

# =====================
# 计算总成绩
# =====================
df["Total"] = df["Math"] + df["English"] + df["Python"]
print(f"总成绩为：{df[["Name","Total"]]}")
print("--------------------------------------------------------------------------------")

# =====================
# 找总成绩最高的人
# =====================
print(f"总成绩最高的人是：{df.loc[df["Total"].idxmax()]}")

print("--------------------------------------------------------------------------------")
# =====================
# 总成绩分布直方图hist
# =====================
df["Total"].hist()
plt.title("Hist of Total Scores")
plt.xlabel("Total Scores")
plt.ylabel("Count")
plt.show()

# =====================
# 找科目之间关系(散点图scatter)_Math vs Python &  English vs Python
# ====================
plt.scatter(df["Math"],df["Python"],alpha = 0.5)
plt.title("Relationship between Math and Python")
plt.xlabel("Math")
plt.ylabel("Python")
plt.show()

plt.scatter(df["English"],df["Python"],alpha = 0.5)
plt.title("Relationship between English and Python")
plt.xlabel("English")
plt.ylabel("Python")
plt.show()

# =====================
# 用 describe() 一次看所有统计
# ====================
print(df.describe())