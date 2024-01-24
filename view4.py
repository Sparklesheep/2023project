import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 读取Excel表格数据
df = pd.read_excel('update_commits.xlsx')

# 将时间列转换为日期时间格式
df['time'] = pd.to_datetime(df['time'])

# 设置时间段的起始时间和结束时间
start_time = df['time'].min().replace(minute=0, second=0)
end_time = df['time'].max().replace(minute=0, second=0) + timedelta(hours=1)

# 创建时间段列表
time_periods = pd.date_range(start=start_time, end=end_time, freq='H')

# 统计每个时间段的提交次数
submit_counts = []
for period in time_periods:
    start = period.strftime('%#I:%M%p')
    end = (period + timedelta(hours=1) - timedelta(minutes=1)).strftime('%#I:%M%p')
    count = len(df[(df['time'] >= period) & (df['time'] < period + timedelta(hours=1))])
    submit_counts.append(count)
    period_str = f'{start}-{end}'
    print(f'Time period: {period_str}, Submit count: {count}')

# 绘制折线图
plt.plot(time_periods, submit_counts)

# 设置x轴标签显示格式
plt.xticks(time_periods, [period.strftime('%#I:%M%p') for period in time_periods], rotation=45)

# 设置坐标轴标签
plt.xlabel('Time')
plt.ylabel('Submit Count')

# 显示图形
plt.show()
