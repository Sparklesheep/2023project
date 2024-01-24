import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 读取Excel表格数据
df = pd.read_excel('update_commits.xlsx')

# 将date列转换为日期类型
df['date'] = pd.to_datetime(df['date'])

# 以1个月为一个时间段，统计每个时间段内的提交次数
start_date = min(df['date'])
end_date = max(df['date'])
delta = pd.offsets.MonthBegin(1)
date_range = pd.date_range(start=start_date, end=end_date+delta, freq=delta)
submit_counts = []
for i in range(len(date_range)-1):
    start = date_range[i]
    end = date_range[i+1]-pd.Timedelta(days=1)
    count = ((df['date']>=start) & (df['date']<=end)).sum()
    submit_counts.append(count)

# 绘制柱状图
fig, ax = plt.subplots()
ax.bar(date_range[:-1], submit_counts, width=pd.Timedelta(days=28), align='edge')

# 设置坐标轴标签
ax.set_xlabel('Time')
ax.set_ylabel('Submit Count')

# 显示图形
plt.show()
