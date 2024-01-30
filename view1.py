import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel表格数据
df = pd.read_excel('update_commits.xlsx')

# 统计每个作者的提交次数
author_counts = df['author'].value_counts()

# 筛选出提交次数超过三次的作者
top_authors = author_counts[author_counts > 3]

# 绘制柱状图并调整 x 轴间距和字体大小
plt.bar(top_authors.index, top_authors.values)
plt.xlabel('Author')
plt.ylabel('Submission Count')
plt.title('Top Authors by Submission Count')

# 调整 x 轴刻度的位置，使间距再增大1.5倍，同时字体变小1倍
plt.xticks(ticks=range(len(top_authors)), labels=top_authors.index, fontsize=8/1.5, rotation=60)

plt.show()
