import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 读取Excel表格数据
df = pd.read_excel('update_commits.xlsx')

# 统计每个author出现的次数
author_counts = df['author'].value_counts()

# 筛选提交次数大于三的数据
filtered_df = df[df['author'].map(author_counts)>3]

# 将author转换为数值类型
filtered_df.loc[:, 'author'] = pd.factorize(filtered_df['author'])[0]

# 获取所有符合条件的author和对应的提交次数和comment
authors = []
submit_counts = []
comments = []
for author in filtered_df['author'].unique():
    count = (filtered_df['author'] == author).sum()
    if count > 3:
        authors.append(author)
        submit_counts.append(count)
        comments.append(filtered_df[filtered_df['author'] == author]['comment'].values)

# 转换为NumPy数组并确保形状一致
x = np.array(authors)
y = np.array(submit_counts)
z = np.array([np.mean(c) for c in comments])

# 创建3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(x, y, z)

# 设置x轴刻度标签
author_labels = filtered_df.loc[filtered_df['author'].isin(authors), 'author'].unique()
ax.set_xticks(range(len(authors)))
ax.set_xticklabels(author_labels)

# 设置坐标轴标签
ax.set_xlabel('Author Num')
ax.set_ylabel('Submit Count')
ax.set_zlabel('Average Comment')
plt.xticks(fontsize=9, rotation=30)
# 显示图形
plt.show()
