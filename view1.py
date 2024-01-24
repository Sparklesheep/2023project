import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel表格数据
df = pd.read_excel('update_commits.xlsx')

# 统计每个作者的提交次数
author_counts = df['author'].value_counts()

# 筛选出提交次数超过三次的作者
top_authors = author_counts[author_counts > 3]

# 绘制柱状图
plt.bar(top_authors.index, top_authors.values)
plt.xlabel('Author')
plt.ylabel('Submission Count')
plt.title('Top Authors by Submission Count')
plt.xticks(fontsize=10, rotation=45)  # 设置字体大小和旋转角度，以增大间距
plt.show()